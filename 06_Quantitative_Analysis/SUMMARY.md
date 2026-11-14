# Summary — Six Quantitative Dimensions

All figures are computed from the 110 included studies. Dimensions 1–3 use the coded metadata, dimensions 4–6 use body-text extraction with the thresholds documented in `README.md`. Per-study evidence for dimensions 4–6 is in the corresponding `*_mentions_per_study.csv` files.

## 1. Publication trends by category

Year × research direction:

| Year | MT for LLMs | LLMs for MT | Both | Total |
|---|---:|---:|---:|---:|
| 2020 | 1 | 0 | 0 | 1 |
| 2023 | 3 | 4 | 0 | 7 |
| 2024 | 11 | 3 | 1 | 15 |
| 2025 | 27 | 9 | 5 | 41 |
| 2026 | 29 | 11 | 6 | 46 |
| **Total** | **71** | **27** | **12** | **110** |

Year × primary function:

| Year | Verify | Validate | Assess | Understand | Not labelled | Total |
|---|---:|---:|---:|---:|---:|---:|
| 2020 | 1 | 0 | 0 | 0 | 0 | 1 |
| 2023 | 0 | 0 | 2 | 0 | 5 | 7 |
| 2024 | 2 | 3 | 3 | 1 | 6 | 15 |
| 2025 | 3 | 8 | 8 | 0 | 22 | 41 |
| 2026 | 2 | 8 | 13 | 5 | 18 | 46 |
| **Total** | **8** | **19** | **26** | **6** | **51** | **110** |

Year × application domain:

| Year | Code Generation & Repair | Dialogue & Agentic Systems | Not labelled | Total |
|---|---:|---:|---:|---:|
| 2020 | 0 | 0 | 1 | 1 |
| 2023 | 2 | 0 | 5 | 7 |
| 2024 | 1 | 1 | 13 | 15 |
| 2025 | 7 | 6 | 28 | 41 |
| 2026 | 6 | 14 | 26 | 46 |
| **Total** | **16** | **21** | **73** | **110** |

The MT-for-LLMs direction grows from 3 studies in 2023 to 29 in 2026, a factor of roughly ten, and supplies 64.5% of the corpus. The LLMs-for-MT direction grows more slowly, from 4 to 11, and both-direction studies only appear from 2024 onward. Assess is the only functional category that expands in the final year (13 studies in 2026 against 8 in 2025), while Validate plateaus at 8.

## 2. Venue distribution

| Venue | Count | Share |
|---|---:|---:|
| ICSE | 8 | 7.3% |
| ASE | 6 | 5.5% |
| COMPSAC | 5 | 4.5% |
| PACMSE (FSE/ISSTA) | 5 | 4.5% |
| IEEE AITest | 4 | 3.6% |
| IST | 4 | 3.6% |
| PACMPL (OOPSLA) | 3 | 2.7% |
| JSS | 3 | 2.7% |
| IEEE TSE | 3 | 2.7% |
| ACL, ISET, ICST Workshops, FORGE, APSEC, ACM TOSEM | 2 each | 1.8% each |

Publication types: journal 26 (23.6%), conference 49 (44.5%), workshop 6 (5.5%), arXiv 26 (23.6%), other preprint 1 (0.9%), thesis 2 (1.8%). Peer-reviewed venues together account for 81 studies (73.6%).

## 3. Application-domain distribution

| Application domain | Count | Share |
|---|---:|---:|
| Dialogue & Agentic Systems | 21 | 19.1% |
| Code Generation & Repair | 16 | 14.5% |
| Not labelled | 73 | 66.4% |

Only one third of the corpus names a concrete application domain. Dialogue & Agentic Systems overtakes Code Generation & Repair in 2026 (14 against 6), which reverses the pattern of 2023, when code generation led 2 to 0.

## 4. LLM model distribution

| Model family | Papers | Share of 110 |
|---|---:|---:|
| GPT-4 family (GPT-4 / 4o / 4V) | 45 | 40.9% |
| GPT-3.5 / ChatGPT | 37 | 33.6% |
| LLaMA family (incl. Vicuna / Alpaca / Mistral) | 33 | 30.0% |
| Multimodal / vision-language (GPT-4V / LLaVA / Gemini) | 13 | 11.8% |
| Other proprietary (Claude / PaLM / Bard) | 13 | 11.8% |
| Code-specialised (StarCoder / CodeLlama / CodeGen) | 10 | 9.1% |
| Chinese open-source (Qwen / ChatGLM / Baichuan) | 9 | 8.2% |
| GPT-3 / Codex | 2 | 1.8% |
| None of the above | 24 | 21.8% |

Proprietary models dominate. GPT-4 and ChatGPT appear in 45 and 37 studies respectively, while the largest open-source family, LLaMA, reaches 33. Code-specialised and Chinese open-source models remain marginal at 10 and 9 studies, which is consistent with the small number of studies that name a code-generation domain. Multi-label, so totals exceed 110.

## 5. Types of MRs across studies

| MR type | Papers | Share of 110 |
|---|---:|---:|
| LLMs used to generate or discover MRs | 54 | 49.1% |
| Semantic-preserving input transformation | 26 | 23.6% |
| Equivalence or invariance checking | 24 | 21.8% |
| Human-specified or domain-knowledge MRs | 17 | 15.5% |
| None of the above | 35 | 31.8% |

Coded MT lifecycle activity for the 39 studies that apply MT to software artefacts: automated MR discovery 10, input transformation and test implementation 9, agentic and closed-loop orchestration 9, with the remaining 11 combining two or three activities.

The dominant relation type is LLM-generated. Roughly three times as many studies let a model propose the relation (54) as rely on human-specified or domain-knowledge relations (17), which is the empirical counterpart of the LLMs-for-MT argument in Section 5.

## 6. Comparison of evaluation metrics

| Metric family | Papers | Share of 110 |
|---|---:|---:|
| Accuracy | 62 | 56.4% |
| Precision / recall / F1 | 41 | 37.3% |
| False-positive rate | 27 | 24.5% |
| Cost / efficiency | 24 | 21.8% |
| Coverage | 22 | 20.0% |
| MR violation or failure rate | 18 | 16.4% |
| Statistical tests or correlation | 13 | 11.8% |
| Fault or bug detection rate | 13 | 11.8% |
| Human evaluation | 12 | 10.9% |
| pass@k | 4 | 3.6% |
| Similarity scores | 1 | 0.9% |
| None of the above | 11 | 10.0% |

Accuracy-based reporting is dominant, and 41 studies also report precision, recall or F1. Only 18 studies report an MR violation or failure rate, the metric that actually quantifies what a metamorphic test detects, and only 13 report a fault or bug detection rate. Human evaluation appears in 12 studies and pass@k, the standard metric for code tasks, in 4. The metric vocabulary is therefore concentrated on task-level accuracy rather than on testing effectiveness, which supports the call for standard metrics in Section 6.6.
