"""Verify the evidence package against the local archive of the 110 study PDFs."""
import argparse
import csv
import hashlib
import re
import tempfile
import subprocess
import shutil
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent

def read(name):
    with (ROOT / name).open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))

def normalize(text):
    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r"(?<=\w)-\s*\n(?=[a-z])", "", text)
    return "".join(text.split())

def verify(archive):
    register = read("study_register.csv")
    evidence = read("passage_evidence.csv")
    changes = read("second_pass_changes.csv")
    reread = read("source_review_by_study.csv")
    additions = read("source_reread_changes.csv")
    if len(reread) != 110 or {r["study_no"] for r in reread} != {str(i) for i in range(1,111)}:
        raise ValueError("Incomplete study review")
    entries = read("entry_audit.csv")
    edits = read("entry_changes.csv")
    if len(entries) != 1150 or [int(r["old_evidence_row"]) for r in entries] != list(range(1,1151)):
        raise ValueError("The audit must cover each of the 1,150 baseline records once")
    def membership(row):
        return (row["study_no"], row["dimension"], row["label"], row["passage_id"])
    actual = {membership(r) for r in evidence}
    baseline = {membership(r) for r in entries}
    removals = {membership(entries[int(r["old_row"])-1]) for r in edits if r["old_row"]}
    additions_from_log = {membership(r) for r in edits}
    if (baseline - removals) | additions_from_log != actual or len(evidence) != len(actual):
        raise ValueError("The corrected ledger does not agree with the entry change log")
    if any((r["study_no"],r["corrected_dimension"],r["corrected_label"],r["corrected_passage_id"]) not in actual for r in entries):
        raise ValueError("An audited decision is missing from the corrected ledger")
    bounded = read("bounded_study_counts.csv")
    coverage = {r["study_no"]: r for r in read("review_coverage.csv")}
    wanted = defaultdict(list)
    for row in evidence + changes + additions + reread + bounded + entries + edits:
        wanted[row["study_no"]].append(row)
    total_pages = 0
    for study in register:
        n = study["study_no"]
        pdf = archive / "04_Cross-Validation_and_Final_Inclusion" / "Final_Papers" / study["pdf"]
        if hashlib.sha256(pdf.read_bytes()).hexdigest() != study["pdf_sha256"]:
            raise ValueError(f"Unexpected edition of study {n}")
        with pymupdf.open(pdf) as doc:
            total_pages += len(doc)
            if len(doc) != int(coverage[n]["pdf_pages"]):
                raise ValueError(f"Page count mismatch for study {n}")
            pages = {}
            for row in wanted[n]:
                p = int(row["pdf_page"])
                if p not in pages:
                    pages[p] = " ".join(normalize(b[4]) for b in doc[p - 1].get_text("blocks"))
                if row["study_id"] != study["study_id"] or normalize(row["source_excerpt"]) not in pages[p]:
                    raise ValueError(f"Unmatched passage in study {n}, PDF page {p}")
    with tempfile.TemporaryDirectory() as tmp:
        target = Path(tmp)
        for filename in ("rebuild_counts.py", "study_register.csv", "passage_evidence.csv"):
            shutil.copyfile(ROOT / filename, target / filename)
        subprocess.run([sys.executable, str(target / "rebuild_counts.py")], check=True)
        if (target / "study_counts.csv").read_bytes() != (ROOT / "study_counts.csv").read_bytes():
            raise ValueError("Rebuilt counts differ from the supplied study counts")
    counts = {(r["dimension"], r["label"]): r for r in read("study_counts.csv")}
    for row in read("claim_audit.csv"):
        result = counts[row["dimension"], row["label"]]
        for column, expected in (("study_count", "after"), ("study_numbers", "study_numbers"), ("source_records", "source_records")):
            if result[column] != row[expected]:
                raise ValueError(f"Mismatch in claim audit for {row['label']}")
    print(f"Verified {len(entries)} original audit rows, {len(edits)} latest changes, {len(register)} PDFs, {total_pages} pages, {len(evidence)} evidence rows, "
          f"{len(changes)} previous changes, {len(additions)} new passage decisions, {len(reread)} study notes and {len(bounded)} bounded study counts.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path, help="Local replication repository containing Stage 04")
    verify(parser.parse_args().archive)
