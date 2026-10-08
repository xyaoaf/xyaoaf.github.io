#!/usr/bin/env python3
"""Generate Jekyll publication pages from publications.tsv."""

import argparse
import csv
from datetime import datetime
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_INPUT = SCRIPT_DIR / "publications.tsv"
DEFAULT_OUTPUT = SCRIPT_DIR.parent / "_publications"
REQUIRED_FIELDS = {
    "pub_date",
    "paper_number",
    "title",
    "venue",
    "excerpt",
    "citation",
    "url_slug",
    "paper_url",
    "highlighted",
    "pubtype",
}


def yaml_single_quote(value):
    """Return a YAML-safe single-quoted scalar."""
    return "'" + value.replace("'", "''") + "'"


def parse_bool(value):
    return value.strip().lower() in {"1", "true", "yes", "y"}


def validate_row(row, row_number):
    missing = [field for field in ("pub_date", "paper_number", "title", "venue", "citation", "url_slug", "paper_url") if not row[field].strip()]
    if missing:
        raise ValueError(f"Row {row_number}: missing required values: {', '.join(missing)}")

    try:
        datetime.strptime(row["pub_date"], "%Y-%m-%d")
    except ValueError as error:
        raise ValueError(f"Row {row_number}: pub_date must use YYYY-MM-DD") from error

    if not row["paper_number"].isdigit():
        raise ValueError(f"Row {row_number}: paper_number must be an integer")

    if row["pubtype"].strip() not in {"journal", "proceedings"}:
        raise ValueError(f"Row {row_number}: pubtype must be journal or proceedings")


def render_publication(row):
    year = row["pub_date"][:4]
    lines = [
        "---",
        f'title: "{row["title"].replace(chr(34), "&quot;")}"',
        "collection: publications",
    ]

    # The Publications page lists journal articles and conference proceedings
    # separately, as the CV does; journal is the default and is not written.
    if row["pubtype"].strip() == "proceedings":
        lines.append("pubtype: proceedings")

    if parse_bool(row["highlighted"]):
        lines.append("highlighted: true")

    lines.extend(
        [
            f'permalink: /publication/{year}-{row["url_slug"]}',
            f'date: {row["pub_date"]}',
            f'venue: {yaml_single_quote(row["venue"])}',
            f'paperurl: {yaml_single_quote(row["paper_url"])}',
            f'citation: {yaml_single_quote(row["citation"])}',
            "---",
        ]
    )

    excerpt = row["excerpt"].strip()
    if excerpt:
        lines.insert(-1, f'excerpt: {yaml_single_quote(excerpt)}')

    return "\n".join(lines) + "\n"


def generate(input_path, output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)

    with input_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        fields = set(reader.fieldnames or [])
        if fields != REQUIRED_FIELDS:
            missing = sorted(REQUIRED_FIELDS - fields)
            extra = sorted(fields - REQUIRED_FIELDS)
            details = []
            if missing:
                details.append(f"missing columns: {', '.join(missing)}")
            if extra:
                details.append(f"unexpected columns: {', '.join(extra)}")
            raise ValueError("Invalid TSV header (" + "; ".join(details) + ")")

        written = []
        for row_number, row in enumerate(reader, start=2):
            validate_row(row, row_number)
            filename = f'{row["pub_date"]}-paper-{row["paper_number"]}-{row["url_slug"]}.md'
            destination = output_dir / filename
            destination.write_text(render_publication(row), encoding="utf-8")
            written.append(destination)

    return written


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    written = generate(args.input, args.output_dir)
    for path in written:
        print(path)


if __name__ == "__main__":
    main()
