# Coding Disagreements and Final Labels: 110 Primary Studies

## Scope and summary

This table aligns the previously documented classifications of Daixu Ren and Zenghui Zhou with the final labels for the current corpus of 110 primary studies. All 15 studies in the original disagreement list remain in the current corpus.

| Measure | Number |
|---|---:|
| Primary studies in the current corpus | 110 |
| Studies with a previously documented label disagreement | 15 |
| Documented study-level disagreement proportion | 13.6% (15/110) |
| Studies with a primary-functional disagreement | 11 |
| Studies with a research-direction disagreement | 5 |
| Studies with disagreements in both dimensions | 1 (CHIME) |
| Distinct study–dimension disagreement records | 16 |

The 15 studies comprise 10 with a primary-functional disagreement only, four with a research-direction disagreement only, and one with both. These counts describe the preserved disagreement list, not a new exhaustive comparison of every coding field across all 110 studies. The final-label column records the outcome, rather than replacing either author's previously recorded label.

## Study-level disagreements, adjudication and final labels

The two authors' labels are kept as recorded in the original disagreement report. The outcomes follow the confirmed final classification of the 110 studies (`Final_Classification_110.xlsx`), not the earlier proposed-decision table. The rationale column summarizes the saved full-text evidence, adjudication screenshots and discussion records; it is not a verbatim quotation of the adjudicator. This table introduces no new adjudication.

CHIME is disputed in two dimensions; both decisions are listed, but the study is counted once. Study IDs retain the original coding keys, so the year in a key does not necessarily equal the publication year of the final version. In the decision column, "retained" and "changed" are relative to the label in the submitted manuscript.

| No. | Study and coding key | Disputed dimension | Daixu Ren's label | Zenghui Zhou's label | Adjudicator's decision (Zheng Zheng) | Rationale (summary) | Final label |
|---:|---|---|---|---|---|---|---|
| 1 | Content-quality classification: `chan2024validating` | Primary function | Validate | Verify | Primary function changed to Verify | The study mainly checks whether quality predictions under semantics-preserving transformations satisfy the MRs and counts the violations; it notes that zero violations may still coincide with poor classification accuracy, so relation conformance cannot be equated directly with task correctness (§3.1 and Conclusion). | **Verify** |
| 2 | Sensei: `de2025automated` | Primary function | Validate | Verify | Primary function: Validate retained | End-to-end tests judge the chatbot's functionality, interaction and goal completion under business scenarios and simulated user goals; the DSL/MR rule checks serve these higher-level requirements rather than merely reporting whether the rules pass (§5.6 and §7). | **Validate** |
| 3 | LLM code-reading ability: `li2023evaluating` | Primary function | Validate | Assess | Primary function changed to Assess | The core design systematically compares code-reading accuracy across model versions, prompts and code transformations; the main conclusions concern capability measurement and comparison (Tables II–III and Conclusion). | **Assess** |
| 4 | PCS: `salimian2025pcs` | Primary function | Validate | Assess | Primary function changed to Assess | Prediction consistency under transformations is aggregated into a confidence score; the evaluation mainly covers confidence estimation, classification performance, model combinations and MR ablation, so the core output is quantification and comparison (§3, RQ1–RQ4). | **Assess** |
| 5 | Symmetric MRs in education technology: `chan2024symmetric` | Primary function | Verify | Assess | Primary function changed to Assess | The MRs are mainly used to generate augmented training data; the study compares ACC, MCC and robustness before and after augmentation rather than reporting relation satisfaction or violation as its main conclusion (§III, Table I and §V). | **Assess** |
| 6 | SQLHD: `yang2025sqlhd` | Primary function | Verify | Validate | Primary function changed to Validate | The two-stage MR checks are further used to judge schema-linking and logical-synthesis hallucinations; the final objective is to identify SQL that violates the question intent or task-correctness requirements (§3.1, §3.5–3.6). | **Validate** |
| 7 | CHIME: `tamanna2025chatgpt` | Primary function; research direction | Verify; MT for LLMs | Validate; Both | Primary function changed to Validate; direction: MT for LLMs retained | Function: consistency checks are used to correct answers about technical reports, and the final evaluation concerns correctness and usefulness to users (§VI-C and §VII). Direction: the main objective is testing LLM answers; the existing records do not explicitly confirm that the metamorphic question variants were generated by an LLM, and the automatic CoVe follow-up questions cannot by themselves confirm a Both label. | **Validate; MT for LLMs** |
| 8 | MT-LAPR: `xue2024exploring` | Primary function | Understand | Assess | Primary function: Understand retained | Beyond the R-score comparison, the study separately analyzes how perturbation distance, perturbation content and repair patterns affect failures, and designs improvements on that basis; the analysis of behavior and failure patterns is a substantive contribution (§IV-E, §V–VI and §VIII). | **Understand** |
| 9 | MORPH: `panichella2025metamorphic` | Primary function | Understand | Assess | Primary function changed to Assess | The study mainly compares distillation effectiveness, accuracy, prediction flips, model size, FLOPs and Pareto trade-offs; ablating optimization components does not make explaining LLM behavioral mechanisms its main contribution (§IV, RQ1–RQ3). | **Assess** |
| 10 | Search-based MR selection: `hyun2025search` | Primary function | Understand | Assess | Primary function changed to Assess | The main objective is to compare the effectiveness, efficiency and execution cost of search algorithms; an additional analysis of perturbation patterns across models does not change this main objective of systematic evaluation (§4.1, RQ1–RQ3 and §6). | **Assess** |
| 11 | MeTMaP: `wang2024metmap` | Primary function | Verify | Understand | Primary function: Verify retained | False matches are detected through semantic-distance relations among source sentences, positive examples and negative examples, and the paper treats the relations themselves as its main concern. Analyses such as structural bias are not sufficient to require replacing the primary Verify label with Understand (§3.5 and Discussion). | **Verify** |
| 12 | MetaQA: `yang2025hallucination` | Research direction | MT for LLMs | Both | Direction: MT for LLMs retained | Classified by the main research objective: LLM-generated response variants are a supporting step in metamorphic hallucination detection, and the main contribution is MT for testing LLM hallucinations (§3.2 and Algorithm 1). The decision does not imply that the paper does not use LLMs to generate variants. | **MT for LLMs** |
| 13 | MetaRAG: `sok2025metarag` | Research direction | MT for LLMs | Both | Direction: MT for LLMs retained | Classified by the main research objective: LLM-generated factoid variants support the metamorphic evaluation of the factual reliability of RAG, and the main objective remains MT for testing RAG answers (§3.1–3.4). The decision does not deny that LLMs take part in generating the variants. | **MT for LLMs** |
| 14 | METAL: `hyun2024metal` | Research direction | MT for LLMs | Both | Direction: MT for LLMs retained | Classified by the main research objective: LLM prompt-based perturbations are a component of the testing framework and serve the main objective of assessing LLM quality with MT (§III-C–D). The decision does not imply that there is no LLM-assisted test generation. | **MT for LLMs** |
| 15 | AutoMT: `liang2025automt` | Research direction | Both | LLMs for MT | Direction changed to LLMs for MT | LLM agents automate MR extraction, scenario analysis and test generation; the systems under test are six autonomous-driving vision models, not LLMs (§III and §IV-C). | **LLMs for MT** |

## Final-label distribution within the disputed dimensions

These distributions concern only the studies disputed in the specified dimension; they are not category totals for the full corpus.

| Disputed dimension | Final label | Studies |
|---|---|---:|
| Primary function (11 studies) | Verify | 2 |
| Primary function (11 studies) | Validate | 3 |
| Primary function (11 studies) | Assess | 5 |
| Primary function (11 studies) | Understand | 1 |
| Research direction (5 studies) | MT for LLMs | 4 |
| Research direction (5 studies) | LLMs for MT | 1 |
| Research direction (5 studies) | Both | 0 |

## Evidence and provenance

- The two authors' recorded labels are transcribed from the disagreement report dated 30 September 2026 and its study-level comparison dated 2 October 2026.
- Final labels are taken from the final classification dated 22 October 2026, provided in this folder as `Final_Classification_110.xlsx` (sheet "Final Labels"), not from the earlier proposed-decision table.
- Decision summaries additionally use the saved adjudication-table screenshot dated 12 October 2026, the full-text evidence record dated 4 October 2026, and the confidence-review record dated 12 October 2026. Earlier recommendations that differ from the final labels are not treated as final decisions.
- All 15 titles were checked against the 110-study inclusion list in this folder ([`Final_Included_Studies_110.xlsx`](Final_Included_Studies_110.xlsx)) on 3 November 2026; all matched after normalizing capitalization and punctuation.
- This document preserves the documented disputed cases. It is not a complete per-author initial-label matrix or a complete cross-checking log for all 110 studies. The disagreement count also differs conceptually from the number of classification changes relative to the submitted manuscript.
