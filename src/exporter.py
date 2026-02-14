from __future__ import annotations

from pathlib import Path
import pandas as pd


def export_excel(df: pd.DataFrame, output_path: str) -> str:
    """
    Export DataFrame to Excel (.xlsx).
    """
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    if path.suffix.lower() != ".xlsx":
        path = path.with_suffix(".xlsx")

    df.to_excel(path, index=False)
    return str(path)


def export_csv(df: pd.DataFrame, output_path: str) -> str:
    """
    Export DataFrame to CSV.
    """
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    if path.suffix.lower() != ".csv":
        path = path.with_suffix(".csv")

    df.to_csv(path, index=False, encoding="utf-8")
    return str(path)
