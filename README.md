# Stage Evidence Package

This package is organized by the stages of literature search and screening. It can be read on its own, and all file references point to materials inside the package.

Stage 04 is based on the 110 primary studies listed in `Final_Included_Studies_110.xlsx`. The `Final_Papers` folder contains the corresponding 110 PDFs.

## Directory Structure

- `01_Database_Search_and_Deduplication`
  - `01_Query_Hits_946`: query hit summary for the six databases, per-query details, search strings and scope, and result screenshots.
  - `02_Within-Database_Unique_392`: the 392 records remaining after within-database deduplication, with deduplication keys.
  - `03_Cross-Database_Unique_252`: the 252 records remaining after cross-database deduplication, with merge evidence.
- `02_TAK_Screening`: screening results for the 252 records and the list of 120 records retained.
- `03_Snowballing`: the snowballing stage added after the database search was frozen; lists the 18 supplementary candidates and archives the available PDFs of all 138 candidates.
- `04_Cross-Validation_and_Final_Inclusion`: lists the 110 included primary studies with year and publication-type statistics; the `Final_Papers` folder holds the corresponding 110 PDFs.

## Reading Guide

The query-hit stage starts at `01_Database_Search_and_Deduplication/01_Query_Hits_946/Query_Hits_946.xlsx`. The workbook contains three sheets: "Hit Summary", "Query Details" and "Search Strings and Scope". Screenshots are in the `screenshots` folder in the same directory; the result counts shown in the screenshots add up to 946.

The within-database deduplication stage starts at `01_Database_Search_and_Deduplication/02_Within-Database_Unique_392/Within-Database_Unique_392.xlsx`. The workbook contains two sheets: "Deduplication Summary" and "Record List". The 392 records keep duplicates across databases; cross-database deduplication is handled in the next stage.

The cross-database deduplication stage starts at `01_Database_Search_and_Deduplication/03_Cross-Database_Unique_252/Cross-Database_Unique_252.xlsx`. The workbook contains three sheets: "Deduplication Summary", "Unique Records" and "Merge Details", showing how the 392 records were merged into 252.

The TAK screening stage starts at `02_TAK_Screening/TAK_Screening_120.xlsx`. The workbook contains two sheets: "Screening Summary" and "Screening List". The summary shows that 120 of the 252 records were retained and 132 were excluded; the screening list contains only the 120 retained records, with primary record ID, title, source databases, screening decision and link.

The snowballing stage starts at `03_Snowballing/Snowballing_Additions_18.xlsx`. The list contains the 18 supplementary records, with snowballing ID, title, year, link and note (SB-010 records its version relation); final inclusion was determined in the subsequent review stage.

The `03_Snowballing/138_Candidates_(120+18)` folder archives 137 PDFs, whose file names are prefixed with the MU or SB ID from the lists above. The download entry for the one missing record is given in `Pending_Downloads.xlsx` in the same folder; records whose full text cannot be obtained are excluded later.

`04_Cross-Validation_and_Final_Inclusion/Final_Included_Studies_110.xlsx` lists the title, year and publication information of the 110 included primary studies (formally published studies are recorded by their published version, with the year taken from the journal volume or the conference year). `Statistics_110.md` in the same folder summarizes the distribution by year, by publication type, year × type, and the main publication venues. The `Final_Papers` folder contains the 110 corresponding PDFs, named in the "Year_Title" format. All formally published studies are archived in their published version, with two exceptions: the published versions of MU-0105 (QUATIC 2024, DOI 10.1007/978-3-031-70245-7_9) and MU-0140 (NLDB 2025, DOI 10.1007/978-3-031-97141-9_17) could not be obtained, so their arXiv versions are archived instead (arXiv:2401.17019v3 and arXiv:2504.18827v3, respectively); bibliographic information and citations follow the published versions.
