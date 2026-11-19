# Full-text evidence for Comment 2.5

This review covers the 110 archived PDFs in Stage 04. It supplies evidence for model use, metamorphic relations (MRs) and reported evaluation measures. Study numbers follow the Final Labels workbook. PDF pages start at 1 and include any cover or publisher pages.

## Checking a count

1. Find a category in `study_counts.csv`. Its study numbers, IDs and source records identify what contributed to the total.
2. For a full-text category, locate each source record in `passage_evidence.csv`. A passage can support several labels. Open the named PDF on the recorded page to inspect the surrounding paragraph or table.
3. For a register-based category, follow the study number to `study_register.csv`. The year, direction, application labels, primary function and lifecycle labels come from Stage 04 `Final_Classification_110.xlsx`, joined by study number and title. Publication types are joined by title to the included rows on the Stage 05 Scores sheet. Selected venue is a normalization of the bibliographic entry for the five outlets tabulated here.
4. Run `python3 rebuild_counts.py` in this folder to regenerate the counts from the register and the ledger. The script uses the Python standard library. Distinct studies are the unit of analysis; multiple models, metrics, passages and relation types may occur in a single study.

## What was coded

The study register provides a compact per-paper inventory. The ledger gives positive evidence, with the original wording of the study and normalized text extraction (line wraps, ligatures and discretionary hyphens). Table extracts follow the PDF text layer; consult the original page for its layout. The study register includes filenames and SHA-256 digests. URLs identify the archived editions used for this review.

- **Model or implemented system.** Include an explicitly used target, generator, judge, experimental baseline or component. Named services and end-to-end systems are retained under their own labels. Versions and roles are often more specific in the passage than in the normalized label. Names in previous work, proposed extensions, acknowledgements and lists of unused alternatives provide no evidence of experimental use. An unnamed backend stays unnamed.
- **MR.** Record the transformation or output property supported by the methods or results. A test-input operation, such as demographic substitution, and an expected output property, such as invariance, describe different aspects of a test. A paper can support both. Specific examples are retained alongside category labels. The inventory records evidenced patterns; it is not a transcription of every individual test instantiated in each paper.
- **MR assessed as a candidate.** Use this dimension for examples of proposed or generated relations examined in an MR-quality or identification study. Such an example alone does not establish execution against the target.
- **MR construction.** Examples include inferring a relation, proposing candidates with an LLM, and implementing the input transformation of a given relation. Stage 04's lifecycle taxonomy is tabulated separately. It has its own inclusion rules.
- **Metric.** Record measures actually computed, tabulated or used to assess an experimental outcome. Metric labels preserve distinctions such as false-positive rate versus the proportion of flagged cases that are false, pass@k versus repeated-run reliability, and a count of faults versus a detection rate. Numeric model identifiers and dataset sizes are not performance outcomes. A percentage called “accuracy” only in explanatory prose does not establish a reported accuracy result.
- **Scope note.** Records limitations, plans or boundary cases. These entries do not contribute positive labels to the synthesis.

The OpenAI group includes explicit OpenAI GPT designations, ChatGPT, GPT-OSS, Text-Davinci-003, o1, o3 and o4. GPT-J and GPT-Neo have separate labels. A provider is not inferred solely from a hosting service, a derivative's backbone or a Copilot deployment. The Llama and Qwen counts refer to the normalized labels themselves; smaller named derivatives can be looked up separately. The precision/recall/F1 figure is the union of study IDs across those three labels. Aggregate figures represent confirmed positive records and are lower bounds on use. They do not estimate the frequency of unreported uses, model quality, or the proportion of studies testing a vendor as the primary target.

## Scope cases

Study 8 evaluates scientific-variable extraction upstream of MR discovery. Study 16 uses a generative optimizer (WOGAN). Study 29 tests browser extensions with undisclosed backends. Study 55 explicitly limits its empirical study to PLM-ICD. Study 71 presents TEMPLEs as work in progress. Study 78 describes future specification-driven testing and preliminary work on conversational systems. The register keeps all these studies in the corpus of 110. Empty fields denote no positively coded record in that dimension.

## Second review

The review used the 110 archived PDFs. All 1,734 PDF pages were text-extracted in page order. The reviewer inspected experimental descriptions, named panels, MR definitions, outcome measures, result tables and ambiguous wording across the papers. Fourteen pages with sparse text were also rendered and visually checked. The coverage file distinguishes pages extracted from pages cited. Page extraction and passage verification do not certify an exhaustive line-by-line reading of every article or a second independent coder.

The headline counts represent distinct study records. An explicit numeric baseline result can count even if it is secondary. Threshold optimization alone does not establish a reported F1 result. CodeLlama, CodeQwen, QwQ and R1-Qwen have separate labels. Explicitly named backbones can be recorded when a result table identifies them. Two additional unions make the effect of including the specified derivatives reproducible. They do not purport to identify all architectural descendants. Study 38's attributed Claude answer is a worked example outside the main experimental comparison. WOGAN and Botium are implemented components, not LLMs.

The broad false-positive count requires an experimental result or plot explicitly called false-positive rate or FP rate. References to expected improvement or general ROC terminology do not qualify. Study 8's Figure 5 uses this name while the prose describes counts. The narrower false-positive rate code retains studies 24 and 96, for correct programs and nonfaulty configurations respectively. Study 24 explicitly identifies the denominator. Study 96 separately reports violation rates on nonfaulty configurations and relates those to operational false positives, without giving the full contingency table for every result. Preserve this qualification when using the narrow code. The distinct 'false-positive share among flags' label codes sampled positives. 'False alarm rate per executable MTC' in studies 30 and 77 has a further, different denominator.

* `second_pass_changes.csv` records each added or withdrawn passage–label decision, including strengthened anchors, the exact paper, PDF page and text.
* `count_changes.csv` compares the distinct-study sets. Blank baseline counts indicate newly tabulated categories.
* `review_coverage.csv` tracks extraction and evidence coverage for every PDF.
* `claim_audit.csv` lists the English draft's empirical headline counts, study memberships, changes, and the status of each estimate.
* `bounded_study_counts.csv` records exact statements within an explicitly defined experimental scope.
* `verify_evidence.py` checks the released rows against the PDFs and their recorded hashes. Run it with a path to the evidence repository and PyMuPDF installed. Run `python3 rebuild_counts.py` to reproduce the distinct-study totals.

## Verification notes

Study 28 (pp. 7–8) uses Partial Pass@k and Worst@10. The reported 98% refers to a partial-pass result. The accuracy count excludes this paper, as does the union of studies reporting pass@1 or pass@5. Those three studies are 40, 47 and 80. The shared notation spans different tasks. Study 106 (pp. 2 and 7) reports third-party gateway aliases for GPT and Claude and qualifies the upstream checkpoint identities. Both labelled-family totals include the deployment. The metadata cell references are in `register_sources.csv`.

## Source review of 19 November

Each of the 110 archived PDFs was reopened and its hash checked. The texts were extracted by page. Methods, experimental roles, outcome definitions and results were revisited across the corpus. Selected tables and examples were also checked against page images. Search assisted retrieval; the decision uses the paper's own description or results. This is targeted rereading and does not certify exhaustive independent double coding.

* `source_review_by_study.csv` contains one row per paper with a focused reading note, a page anchor and the current inventory in all three dimensions. The full set of anchors supporting that inventory is in `passage_evidence.csv`.
* `source_reread_changes.csv` lists new passage–label decisions relative to the 18 November snapshot. `source_reread_count_changes.csv` shows the corresponding changes in distinct study membership. The older `second_pass_changes.csv` remains a historical log. `count_changes.csv` bridges the first snapshot to the current one. In this release `claim_audit.csv` uses the immediately preceding snapshot for its before column.
* The raw MR violation result counts explicit numeric or graphical results on tested units violating an expected relation, including authors' equivalent ASR and FDR definitions. Study 67 computes a raw rate inside a quality-weighted objective (pp. 6, 9–10, 16). Study 95 reports a capability score in the satisfaction direction (p. 14). Study 66 explicitly distinguishes its reflection oracle from MT (p. 11). These cases are outside the raw-result total.
* Accuracy uses a reported correctness outcome, including secondary evaluation panels. Study 65's validation threshold, study 82's SQL labelling rule and study 56's mean cosine-similarity score are kept separate. The precision/recall/F1 total is the union of those three normalized labels. Study 21's retrieval R-Precision and study 104's components of a weighted tool-sequence score retain distinct labels. The broad false-positive terminology total includes qualitative interpretations of the authors' own experimental results (e.g. study 82) as well as plots and numerical results. It does not imply the denominator is shared.
* The substitution count requires evidence of an applied replacement involving identity or a demographic proxy. Study 86 defines swaps but illustrates additions (pp. 7, 12–13); study 62 reports changes of demographic speaking style (pp. 3–5). Both are coded at the specificity supported by the examples. Separate papers may share authors, methods or data; the unit here is the individual publication.

## Entry-level review of 19 November

To reproduce the revised counts, use the PDF-filename and hash register in this folder, the corrected evidence ledger and the distinct-study count script.

`entry_audit.csv` covers all 1,150 entries of the previous passage ledger, including their original classifications, PDF anchors, adjoining text and decisions. `entry_changes.csv` gives all reclassifications and supplemental evidence. `entry_count_changes.csv` compares memberships to the immediately preceding snapshot; `claim_audit.csv` gives the current headline counts against that same snapshot. The two previous change logs describe their dated reviews. Current classifications can be found in `study_register.csv` and `passage_evidence.csv`. The release includes 1,169 passage–label records. The Bonferroni adjustment has its own statistical-procedure dimension in the detailed ledger.
 
Accuracy includes results authors explicitly report as accuracy for selected experimental subsets; study 69 measures correctness among manually checked seeds already deemed valid. Study 87 contributes a rate for applicable snippets judged against author-defined MRs, without requiring two executed inputs for each judgment. The 32-paper result includes that operationalization and should not be described as 32 reports of paired-execution failure rates. For model counts an explicitly named component, such as study 40's GPT-2 decoder, can qualify. No independent upstream identity is asserted for gateway aliases.

`rebuild_counts.py` summarizes released classifications; it has no PDF-to-classification stage. For semantic decisions, follow the page and the experimental role in the source.
