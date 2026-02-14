from __future__ import annotations

from pathlib import Path
import pandas as pd


SUPPORTED_EXTS = {".csv", ".xlsx", ".xls"}


def load_file(file_path: str) -> pd.DataFrame:
    """
    Load a CSV or Excel file into a DataFrame.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if path.suffix.lower() not in SUPPORTED_EXTS:
        raise ValueError(f"Unsupported file type: {path.suffix}. Use CSV or Excel.")

    if path.suffix.lower() == ".csv":
        # Try utf-8 first, fallback to latin-1 for messy CSVs
        try:
            df = pd.read_csv(path, encoding="utf-8")
        except UnicodeDecodeError:
            df = pd.read_csv(path, encoding="latin-1")
        return df

    # Excel
    return pd.read_excel(path)
