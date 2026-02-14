from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

import pandas as pd

from loader import load_file
from cleaner import normalize_columns, drop_empty_rows, trim_strings, coerce_numeric
from sorter import sort_dataframe
from ranker import add_rank, top_n
from exporter import export_excel, export_csv


DEFAULT_DATA_PATH = Path("data/responses.xlsx")
OUTPUT_DIR = Path("output")


def _print_cols(df: pd.DataFrame) -> None:
    print("\nAvailable columns:")
    for i, c in enumerate(df.columns, start=1):
        print(f"  {i:>2}. {c}")
    print("")


def _ask_path() -> str:
    raw = input(f"Enter file path (or press Enter for default: {DEFAULT_DATA_PATH}): ").strip()
    return str(DEFAULT_DATA_PATH) if raw == "" else raw


def _ask_yes_no(prompt: str) -> bool:
    while True:
        ans = input(prompt + " (y/n): ").strip().lower()
        if ans in {"y", "yes"}:
            return True
        if ans in {"n", "no"}:
            return False
        print("Please type y or n.")


def _ask_int(prompt: str, min_val: int | None = None, max_val: int | None = None) -> int:
    while True:
        raw = input(prompt + ": ").strip()
        try:
            val = int(raw)
            if min_val is not None and val < min_val:
                print(f"Must be >= {min_val}")
                continue
            if max_val is not None and val > max_val:
                print(f"Must be <= {max_val}")
                continue
            return val
        except ValueError:
            print("Enter a valid integer.")


def _choose_columns(df: pd.DataFrame) -> list[str]:
    _print_cols(df)
    print("Choose columns to sort by (comma-separated numbers). Example: 1,3")
    raw = input("Your choice: ").strip()
    if not raw:
        raise ValueError("No columns selected.")
    idxs = []
    for part in raw.split(","):
        part = part.strip()
        if not part:
            continue
        idxs.append(int(part))
    cols = []
    for i in idxs:
        if i < 1 or i > len(df.columns):
            raise ValueError("Invalid column index.")
        cols.append(df.columns[i - 1])
    return cols


def _choose_single_column(df: pd.DataFrame, title: str) -> str:
    _print_cols(df)
    i = _ask_int(f"{title} - enter column number", 1, len(df.columns))
    return df.columns[i - 1]


def _apply_optional_filter(df: pd.DataFrame) -> pd.DataFrame:
    if not _ask_yes_no("Do you want to filter rows by a column value?"):
        return df

    col = _choose_single_column(df, "Filter")
    value = input(f"Enter the value to match for '{col}' (case-insensitive): ").strip().lower()

    out = df.copy()
    # Convert to string for matching; NaN-safe
    mask = out[col].astype(str).str.lower().eq(value)
    filtered = out[mask].reset_index(drop=True)

    print(f"Filtered rows: {len(filtered)} (from {len(df)})")
    return filtered


def main():
    print("\n=== Student Data Automation & Ranking System (Python) ===")

    try:
        path = _ask_path()
        df = load_file(path)

        print(f"\nLoaded data: {df.shape[0]} rows × {df.shape[1]} columns")

        # Cleaning pipeline
        df = normalize_columns(df)
        df = drop_empty_rows(df)
        df = trim_strings(df)

        # Try to coerce common numeric columns if they exist
        common_numeric_cols = ["score", "marks", "cgpa", "percentage"]
        df = coerce_numeric(df, common_numeric_cols)

        print("\nColumns normalized + basic cleaning done.")
        _print_cols(df)

        df = _apply_optional_filter(df)

        # Sorting
        sort_cols = _choose_columns(df)
        asc = _ask_yes_no("Sort ascending? (No means descending)")
        df_sorted = sort_dataframe(df, sort_cols=sort_cols, ascending=asc)

        print("\nSorted successfully. Preview (first 8 rows):")
        print(df_sorted.head(8).to_string(index=False))

        # Ranking (optional)
        if _ask_yes_no("\nDo you want to add ranking (Top N) based on a score column?"):
            score_col = _choose_single_column(df_sorted, "Ranking score")
            higher_is_better = _ask_yes_no("Higher score is better?")
            df_ranked = add_rank(df_sorted, score_col=score_col, higher_is_better=higher_is_better)
            n = _ask_int("Enter N for Top N", 1, max(1, len(df_ranked)))
            df_final = top_n(df_ranked.sort_values("rank"), n)
        else:
            df_final = df_sorted

        # Export
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        out_base = OUTPUT_DIR / f"results_{ts}"

        out_excel = export_excel(df_final, str(out_base.with_suffix(".xlsx")))
        print(f"\n✅ Exported Excel to: {out_excel}")

        if _ask_yes_no("Also export CSV?"):
            out_csv = export_csv(df_final, str(out_base.with_suffix(".csv")))
            print(f"✅ Exported CSV to: {out_csv}")

        print("\nDone. You can upload the Excel/CSV output in your LinkedIn 'Featured' or GitHub releases.")
        return 0

    except Exception as e:
        print("\n❌ Error:", str(e))
        return 1


if __name__ == "__main__":
    sys.exit(main())
