#!/usr/bin/env python3
"""Quantitative analysis of the 110 included studies (Comment 2.5).

Inputs (from the evidence repository):
  04_Cross-Validation_and_Final_Inclusion/Final_Classification_110.xlsx
  04_Cross-Validation_and_Final_Inclusion/Final_Included_Studies_110.xlsx
  04_Cross-Validation_and_Final_Inclusion/Statistics_110.md
  04_Cross-Validation_and_Final_Inclusion/Final_Papers/*.pdf

Run:  python3 analysis_script.py   (requires pymupdf + openpyxl)

By default the evidence repository is taken to be the parent directory of this
folder; set EVID to point at the repository when it lives elsewhere.
"""
import os, re, csv, collections

OUT = os.path.dirname(os.path.abspath(__file__))
EVID = os.environ.get('EVID', os.path.abspath(os.path.join(OUT, '..')))
PDF = f'{EVID}/04_Cross-Validation_and_Final_Inclusion/Final_Papers'

# ---------- helpers ----------
def write_csv(fn, header, recs):
    with open(os.path.join(OUT, fn), 'w', newline='', encoding='utf-8-sig') as fh:
        w = csv.writer(fh); w.writerow(header)
        for r in recs: w.writerow(r)

def safe(n):
    return re.sub(r'[^\w\-. ]', '_', n[:-4]) + '.txt'

def body(t):
    """Drop the reference list before matching."""
    m = re.search(r'\n\s*(References|REFERENCES|Bibliography)\s*\n', t)
    return t[:m.start()] if m else t

def extract_texts():
    import pymupdf, tempfile
    d = tempfile.mkdtemp()
    for f in sorted(os.listdir(PDF)):
        if not f.endswith('.pdf'): continue
        doc = pymupdf.open(os.path.join(PDF, f))
        t = ''.join(p.get_text() for p in doc); doc.close()
        open(os.path.join(d, safe(f)), 'w', encoding='utf-8').write(t)
    return d

# ---------- study metadata ----------
import openpyxl
wb = openpyxl.load_workbook(f'{EVID}/04_Cross-Validation_and_Final_Inclusion/Final_Classification_110.xlsx', data_only=True)
ws = wb['Final Labels']
hdr = [(c.value or '').strip().replace('\n', ' ') for c in ws[8]]
idx = {h: i for i, h in enumerate(hdr)}
rows = [r for r in ws.iter_rows(min_row=9, values_only=True) if r[idx['No.']]]

def c(r, name):
    v = r[idx[name]]
    return str(v).strip() if v is not None else ''

studies = [{
    'no': c(r, 'No.'), 'sid': c(r, 'Study ID (coding key)'), 'title': c(r, 'Title'),
    'year': c(r, 'Year'), 'direction': c(r, 'Research direction'),
    'function': c(r, 'Primary function'), 'quality': c(r, 'Quality attribute'),
    'domain': c(r, 'Application domain (MT-for-LLMs branch)'),
    'lifecycle': c(r, 'MT lifecycle activity'),
} for r in rows]
assert len(studies) == 110, len(studies)

# ---------- 1. publication trends by category ----------
years = sorted({s['year'] for s in studies})
dirs = ['MT for LLMs', 'LLMs for MT', 'Both']
write_csv('01a_publication_trend_by_direction.csv', ['Year'] + dirs + ['Total'],
          [[y] + [sum(1 for s in studies if s['year'] == y and s['direction'] == d) for d in dirs]
           + [sum(1 for s in studies if s['year'] == y)] for y in years])

write_csv('01b_direction_totals.csv', ['Direction', 'Paper count'], [
    ['MT for LLMs (both-direction papers included)', sum(1 for s in studies if s['direction'] in ('MT for LLMs', 'Both'))],
    ['LLMs for MT (both-direction papers included)', sum(1 for s in studies if s['direction'] in ('LLMs for MT', 'Both'))],
    ['Both directions', sum(1 for s in studies if s['direction'] == 'Both')],
    ['Total distinct studies', 110],
])

fns = ['Verify', 'Validate', 'Assess', 'Understand', '(not labelled)']
write_csv('01c_publication_trend_by_function.csv', ['Year'] + fns + ['Total'],
          [[y] + [sum(1 for s in studies if s['year'] == y and (s['function'] or '(not labelled)') == k) for k in fns]
           + [sum(1 for s in studies if s['year'] == y)] for y in years])

doms = ['Code Generation & Repair', 'Dialogue & Agentic Systems', '(not labelled)']
write_csv('01d_publication_trend_by_application_domain.csv', ['Year'] + doms + ['Total'],
          [[y] + [sum(1 for s in studies if s['year'] == y and (s['domain'] or '(not labelled)') == k) for k in doms]
           + [sum(1 for s in studies if s['year'] == y)] for y in years])

# ---------- 2. venue & publication type ----------
md = open(f'{EVID}/04_Cross-Validation_and_Final_Inclusion/Statistics_110.md', encoding='utf-8').read()
def md_table(section):
    return re.findall(r'^\|\s*([^|*][^|]*?)\s*\|\s*(\d+)\s*\|\s*([\d.]+%)\s*\|',
                     md.split(section)[1].split('##')[0], re.M)
write_csv('02a_venue_distribution.csv', ['Venue', 'Count', 'Share'],
          [[v.strip(), int(n), s] for v, n, s in md_table('## 4. Main Publication Venues')])
write_csv('02b_publication_type.csv', ['Publication type', 'Count', 'Share'],
          [[v.strip(), int(n), s] for v, n, s in md_table('## 2. Distribution by Publication Type')])

# ---------- 3. application domain ----------
dom = collections.Counter(s['domain'] or '(not labelled)' for s in studies)
write_csv('03_application_domain.csv', ['Application domain', 'Count', 'Share'],
          [[k, v, f'{v/110*100:.1f}%'] for k, v in dom.most_common()])
qual = collections.Counter(s['quality'] or '(not labelled)' for s in studies)
write_csv('03b_quality_attribute.csv', ['Quality attribute (multi-label)', 'Count', 'Share'],
          [[k, v, f'{v/110*100:.1f}%'] for k, v in qual.most_common()])

# ---------- 4/5/6 need full text ----------
txtdir = extract_texts()
tmap = {f[:-5]: open(os.path.join(txtdir, f), encoding='utf-8').read() for f in os.listdir(txtdir)}
def key_for(s):
    k = f"{s['year']}_{s['title']}"
    if k in tmap: return k
    n = lambda x: re.sub(r'[^a-z0-9]', '', x.lower())
    for cand in tmap:
        if n(re.sub(r'^\d{4}_', '', cand)) == n(s['title']): return cand
    for cand in tmap:
        if n(re.sub(r'^\d{4}_', '', cand))[:40] == n(s['title'])[:40]: return cand
    return None

def analyse(lexicon, threshold, fname_detail, fname_sum, labels):
    det, cnt, none = [], collections.Counter(), 0
    for s in studies:
        k = key_for(s)
        if not k: continue
        t = body(tmap[k]); hit = 0
        for fam, rx in lexicon.items():
            n = len(re.findall(rx, t))
            if n >= threshold:
                m = re.search(rx, t)
                det.append([s['no'], s['sid'], s['title'], s['year'], fam, n,
                            t[max(0, m.start() - 90):m.start() + 110].replace('\n', ' ')])
                cnt[fam] += 1; hit += 1
        if hit == 0: none += 1
    write_csv(fname_detail, ['No.', 'Study ID', 'Title', 'Year', labels[0], 'Occurrences in body', 'Evidence snippet'], det)
    write_csv(fname_sum, [labels[0], f'Papers (>={threshold} occurrences in body)', 'Share of 110'],
              [[k, v, f'{v/110*100:.1f}%'] for k, v in cnt.most_common()]
              + [[f'(none of the {labels[1]} above)', none, f'{none/110*100:.1f}%']])
    return cnt, none

MODEL = {
 'GPT-4 family (GPT-4 / 4o / 4V)': r'(?i)\bGPT[\s-]?4(?:o|v)?\b|\bGPT4\b',
 'GPT-3.5 / ChatGPT': r'(?i)\bGPT[\s-]?3\.5\b|\bChatGPT\b',
 'GPT-3 / Codex': r'(?i)\bGPT[\s-]?3\b(?!\.5)|\bCodex\b|\bdavinci\b',
 'LLaMA family (incl. Vicuna / Alpaca / Mistral)': r'(?i)\bLLa?MA\b|\bVicuna\b|\bAlpaca\b|\bMistral\b|\bMixtral\b',
 'Code-specialised LLMs (StarCoder / CodeLlama / CodeGen)': r'(?i)\bStarCoder\b|\bCodeLlama\b|\bDeepSeek[\s-]?Coder\b|\bCodeGen\b|\bCodeT5\b',
 'Multimodal / vision-language (GPT-4V / LLaVA / Gemini)': r'(?i)\bGPT[\s-]?4V\b|\bLLaVA\b|\bBLIP\b|\bCLIP\b|\bGemini\b',
 'Other proprietary (Claude / PaLM / Bard)': r'(?i)\bClaude\b|\bPaLM\b|\bBard\b',
 'Chinese open-source (Qwen / ChatGLM / Baichuan)': r'(?i)\bQwen\b|\bChatGLM\b|\bBaichuan\b',
}
mc, mnone = analyse(MODEL, 3, '04a_model_mentions_per_study.csv', '04b_model_distribution.csv', ('Model family', 'families'))

MR = {
 'LLMs used to generate / discover MRs': r'(?i)(generate|generat\w*|discover\w*|mine)[^.]{0,60}(metamorphic relation|MR)',
 'Human-specified or domain-knowledge MRs': r'(?i)(manual\w*|hand[- ]craft\w*|human[- ]craft\w*|expert\w*)[^.]{0,60}(metamorphic relation|MR)|domain[- ]specific (metamorphic|MR)',
 'Semantic-preserving input transformation': r'(?i)semantic[- ]preserving|input transformation|transformation operator',
 'Equivalence / invariance checking': r'(?i)equivalence relation|invarian',
}
mrc, mrnone = analyse(MR, 2, '05a_mr_type_mentions_per_study.csv', '05b_mr_type_distribution.csv', ('MR type', 'types'))

life = collections.Counter(s['lifecycle'] or '(not applicable, MT-for-LLMs branch)' for s in studies)
write_csv('05c_mt_lifecycle_activity.csv', ['MT lifecycle activity (coded label)', 'Count', 'Share'],
          [[k, v, f'{v/110*100:.1f}%'] for k, v in life.most_common()])
write_csv('05d_mt_lifecycle_per_study.csv',
          ['No.', 'Study ID', 'Title', 'MT lifecycle activity (as coded)'],
          [[s['no'], s['sid'], s['title'], s['lifecycle']] for s in studies if s['lifecycle']])

MET = {
 'Accuracy': r'(?i)\baccuracy\b',
 'Precision / Recall / F1': r'(?i)\b(precision|recall|f1[- ]?score)\b',
 'pass@k': r'(?i)pass@\d+',
 'MR violation / failure rate': r'(?i)(metamorphic|MR)[^.]{0,40}(violation|failure)\b',
 'Fault / bug detection rate': r'(?i)detection rate|bugs? (found|detected)|faults? (found|detected)',
 'Coverage': r'(?i)(code|branch|statement|test|line|instruction) coverage|coverage (rate|criteria|of)',
 'False-positive rate': r'(?i)false[- ]positive|false alarm',
 'Human evaluation': r'(?i)human (evaluation|study|judge|rating|review|annotation)',
 'Agreement / consistency (kappa, IoU)': r"(?i)cohen'?s kappa|\biou\b|inter[- ]annotator",
 'Similarity scores (BLEU / ROUGE / BERTScore)': r'(?i)\bbelu\b|\brouge\b|\bbertscore\b|\bmeteor\b|\bchrf\b',
 'Statistical tests / correlation': r'(?i)wilcoxon|spearman|pearson|p\s*<\s*0\.0',
 'Cost / efficiency': r'(?i)token (cost|usage|count)|\blatency\b|time cost|api cost|runtime',
}
metc, metnone = analyse(MET, 2, '06a_metric_mentions_per_study.csv', '06b_metric_distribution.csv', ('Metric family', 'families'))

# ---------- cross-tab: models by direction (for the discussion) ----------
dirmap = {s['sid']: s['direction'] for s in studies}
rows = list(csv.DictReader(open(os.path.join(OUT, '04a_model_mentions_per_study.csv'), encoding='utf-8-sig')))
print('done:', len(studies), 'studies')
print('model  :', mc.most_common(), '| none:', mnone)
print('mr     :', mrc.most_common(), '| none:', mrnone)
print('metric :', metc.most_common(), '| none:', metnone)
