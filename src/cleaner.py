from __future__ import annotations

import re
import pandas as pd


def _normalize_col(col: str) -> str:
    """
    Normalize column names:
    - lower
    - trim
    - replace non-alphanum with underscore
    - collapse multiple underscores
    """
    col = str(col).strip().lower()
    col = re.sub(r"[^a-z0-9]+", "_", col)
    col = re.sub(r"_+", "_", col).strip("_")
    return col


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns a copy of df with normalized column names.
    """
    out = df.copy()
    out.columns = [_normalize_col(c) for c in out.columns]
    return out


def coerce_numeric(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    """
    Convert specified columns to numeric if present.
    Non-convertible values become NaN.
    """
    out = df.copy()
    for c in cols:
        if c in out.columns:
            out[c] = pd.to_numeric(out[c], errors="coerce")
    return out


def drop_empty_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    Drop rows that are fully empty.
    """
    return df.dropna(how="all").reset_index(drop=True)


def trim_strings(df: pd.DataFrame) -> pd.DataFrame:
    """
    Strip whitespace from object columns.
    """
    out = df.copy()
    for c in out.columns:
        if out[c].dtype == "object":
            out[c] = out[c].astype(str).str.strip()
            # Convert "nan" strings back to actual NaN (common after astype(str))
            out.loc[out[c].str.lower().isin(["nan", "none", "null", ""]), c] = pd.NA
    return out
