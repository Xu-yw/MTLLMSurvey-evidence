"""Rebuild study-level counts from the released passage ledger and study register."""
import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def read(filename):
    with (ROOT / filename).open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def build():
    register = read("study_register.csv")
    studies = {int(row["study_no"]): row for row in register}
    if len(register) != 110 or set(studies) != set(range(1, 111)):
        raise ValueError("The register must contain exactly studies 1–110.")
    memberships = defaultdict(set)
    anchors = defaultdict(set)

    def add(section, label, number, anchor):
        key = (section, label)
        memberships[key].add(number)
        anchors[key].add(anchor)

    for number, row in studies.items():
        ref = f"S{number:03}:register"
        add("corpus", "all included studies", number, ref)
        if row["year"] in {"2025", "2026"}:
            add("pooled years", "2025–2026", number, ref)
        for branch in ["MT for LLMs", "LLMs for MT"]:
            if row["direction"] in {branch, "Both"}:
                add("inclusive direction", branch, number, ref)
                add("inclusive year by direction", row["year"] + " / " + branch, number, ref)
        if row["quality_attribute"]:
            add("application perspective", "any quality attribute", number, ref)
        if row["application_domain"]:
            add("application perspective", "any application domain", number, ref)
        if row["primary_function"]:
            add("primary function", "any primary function", number, ref)
        if row["lifecycle"]:
            add("lifecycle", "any lifecycle label", number, ref)
        for field in ("year", "direction", "primary_function", "publication_type",
                      "publication_group", "selected_venue", "application_domain"):
            if row[field]:
                add(field, row[field], number, ref)
        for field in ("quality_attribute", "lifecycle"):
            for label in filter(None, map(str.strip, row[field].split(";"))):
                add(field, label, number, ref)
        if row["quality_attribute"] or row["application_domain"]:
            add("application perspective", "one or both", number, ref)
        if row["quality_attribute"] and row["application_domain"]:
            add("application perspective", "both", number, ref)
        add("year by direction", row["year"] + " / " + row["direction"], number, ref)

    groups = {
        "OpenAI-labelled model": {"ChatGPT", "GPT", "GPT-1", "GPT-3.5", "GPT-4", "GPT-5", "GPT-OSS", "Text-Davinci-003", "GPT-2", "o1", "o3", "o4"},
        "Reported pass@k including fixed k": {"pass@1", "pass@5", "pass@k"},
        "ChatGPT or GPT-3.5": {"ChatGPT", "GPT-3.5"},
        "Llama including CodeLlama": {"Llama", "CodeLlama"},
        "Qwen including named derivatives": {"Qwen", "CodeQwen", "R1-Qwen", "QwQ"},
        "Precision, recall or F1": {"precision", "recall", "F1"},
        "Semantic preservation or invariance explicitly coded": {
            "invariance", "semantic invariance", "semantics-preserving code transformation",
            "label invariance", "semantic invariance under paraphrase", "semantics-preserving formula transformation",
            "meaning-preserving and meaning-altering perturbations", "format invariance",
        },
    }
    for row in read("passage_evidence.csv"):
        number = int(row["study_no"])
        if row["study_id"] != studies[number]["study_id"] or not row["source_excerpt"].strip() or int(row["pdf_page"]) < 1:
            raise ValueError(f"Invalid anchor for study {number}")
        dimension, label, ref = row["dimension"], row["label"], row["passage_id"]
        if dimension == "scope note":
            continue
        add(dimension, label, number, ref)
        add("anchored studies", dimension, number, ref)
        for group, labels in groups.items():
            if label in labels:
                add("synthesis", group, number, ref)

    with (ROOT / "study_counts.csv").open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["dimension", "label", "study_count", "study_numbers", "study_ids", "source_records"])
        for key in sorted(memberships):
            numbers = sorted(memberships[key])
            writer.writerow([*key, len(numbers), "; ".join(map(str, numbers)),
                             "; ".join(studies[n]["study_id"] for n in numbers),
                             "; ".join(sorted(anchors[key]))])


if __name__ == "__main__":
    build()
