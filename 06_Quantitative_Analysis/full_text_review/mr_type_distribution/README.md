# Evidence for MR types in Comment 2.5(5)

**(5) Types of MRs.** The evidence table identifies 26 studies that described synonym substitution or synonymous rewriting, 11 that described semantics-preserving code changes, and 13 that described substitutions of demographic attributes or their proxies, such as personal names. The relations also differed in the behavior they required of the output. For example, converting two dates to a different format should preserve the interval between them. The table identifies 14 studies that specified a direction of change or an ordering between outputs. In sentiment analysis, for instance, adding a negative phrase should not make the predicted sentiment more positive. Studies could contribute to more than one count.

## How to trace a count

[counts.csv](counts.csv) lists each group and its contributing studies. [evidence.csv](evidence.csv) gives one row per group and study, with the paper title, a short quotation, the PDF page starting at 1, and a link to that page in the archived edition. Rows added during the handoff check are identified in both tables. [examples.csv](examples.csv) documents the date-format and sentiment examples. The date example illustrates interval preservation and adds no study to the four counts.

The counts describe the positive evidence recorded here. They cover selected overlapping patterns in the survey. The first three groups concern what changes in the input. The fourth concerns the expected output. Each study counts once in each applicable group. Descriptions can appear in a method, a concrete proposal, a candidate assessed in the paper, or an experiment. Recording a candidate does not establish that it passed, was executed, or was accepted as valid.

| Group | Inclusion rule |
| --- | --- |
| synonym | The study describes substituting synonymous natural-language words or expressions in a text, question, prompt, or response. A generic paraphrase or a source-code identifier rename alone is insufficient. |
| code | The study describes changes to program code designed to preserve its semantics. The count concerns the design intent. |
| demographic | A demographic term, attribute value or proxy is exchanged for another. Merely adding or deleting a demographic descriptor is insufficient. |
| direction | A study specifies an expected increase, decrease, non-increase, non-decrease or ordering between outputs for related inputs. Invariance, an unspecified change or a fixed similarity threshold alone is insufficient. |

The source register and archived PDF editions are pinned to commit `1d57e9181fb6a97a19f36d233d3b2b54ed1b3d45`. Some earlier ledger entries use narrower labels or describe another aspect of the same paper. The four totals here are reconstructed from this supplement. The earlier ledger remains available for the original coding.

## Reproduce

Run `python3 verify_counts.py` from this directory. To verify the quotations too, install PyMuPDF and run `python3 verify_counts.py --pdf-root /path/to/Final_Papers` using the Stage 04 archive. The checker recomputes memberships, checks the change lists, checks PDF hashes and searches the cited pages after text normalization. The coding rules above govern how a passage is interpreted.
