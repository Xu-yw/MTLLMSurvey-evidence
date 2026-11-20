"""Rebuild paper-level MR counts and optionally check their archived source pages."""
import argparse
import csv
import hashlib
from pathlib import Path
import re
import unicodedata
from collections import defaultdict
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent


def read(name):
    with (HERE / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def normalize(text):
    text = unicodedata.normalize("NFKC", text).replace("\u00ad", "")
    text = re.sub(r"(?<=\w)-[ \t]*\n(?=[a-z])", "", text)
    return "".join(text.split())


def verify_pages(root, by_file):
    import pymupdf

    for filename, rows in by_file.items():
        path = root / filename
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        with pymupdf.open(path) as document:
            for row in rows:
                page = int(row["pdf_page"])
                label = f"{row['study_id']}, PDF page {page}"
                require(digest == row["pdf_sha256"], f"Edition mismatch: {label}")
                require(1 <= page <= len(document), f"Invalid page: {label}")
                pdf_page = document[page - 1]
                candidates = [pdf_page.get_text(), "\n".join(b[4] for b in pdf_page.get_text("blocks"))]
                excerpt = normalize(row["excerpt"])
                require(any(excerpt in normalize(t) for t in candidates), f"Excerpt mismatch: {label}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf-root", type=Path, help="Stage 04 Final_Papers directory")
    args = parser.parse_args()
    members = defaultdict(set)
    added = defaultdict(set)
    papers = {}
    numbers = {}
    by_file = defaultdict(list)
    evidence = read("evidence.csv")
    examples = read("examples.csv")
    for row in evidence + examples:
        n = int(row["study_no"])
        paper = (row["study_id"], row["title"], row["pdf"], row["pdf_sha256"])
        require(papers.setdefault(n, paper) == paper, f"Inconsistent paper: {n}")
        require(numbers.setdefault(row["study_id"], n) == n, f"Duplicate study ID: {n}")
        require(row["excerpt"].strip(), f"Missing quotation: {n}")
        require(unquote(row["source_url"]).endswith("/" + row["pdf"] + "#page=" + row["pdf_page"]), f"Page link mismatch: {n}")
        by_file[row["pdf"]].append(row)
    for row in evidence:
        category, n = row["category"], int(row["study_no"])
        require(n not in members[category], f"Duplicate membership: {category}, {n}")
        members[category].add(n)
        status = row["review_status"]
        require(status in {"added in handoff check", "previously documented"}, f"Unknown status: {status}")
        if status == "added in handoff check":
            added[category].add(n)
    summary = read("counts.csv")
    require(len(summary) == len(members) and {r["category"] for r in summary} == set(members), "Category mismatch")
    for row in summary:
        category = row["category"]
        listed = [int(n) for n in row["study_numbers"].split()]
        additions = [int(n) for n in row["added_study_numbers"].split()]
        require(sorted(members[category]) == listed and len(listed) == int(row["studies"]), f"Count mismatch: {category}")
        require(sorted(added[category]) == additions and len(listed) - len(additions) == int(row["previously_documented"]), f"Change mismatch: {category}")
        print(f"{category}: {len(listed)} studies")
    if args.pdf_root:
        verify_pages(args.pdf_root, by_file)
        print(f"Verified {len(evidence)} membership quotations and {len(examples)} example quotations.")


if __name__ == "__main__":
    main()
