from __future__ import annotations

import pandas as pd


def add_rank(
    df: pd.DataFrame,
    score_col: str,
    rank_col_name: str = "rank",
    higher_is_better: bool = True,
) -> pd.DataFrame:
    """
    Add a rank column based on a numeric score column.
    Ties get the same rank (dense ranking).
    """
    if score_col not in df.columns:
        raise KeyError(f"Score column '{score_col}' not found.")

    out = df.copy()
    # Convert to numeric safely
    out[score_col] = pd.to_numeric(out[score_col], errors="coerce")

    # rank: dense => 1,2,2,3...
    ascending = not higher_is_better
    out[rank_col_name] = out[score_col].rank(method="dense", ascending=ascending)
    out[rank_col_name] = out[rank_col_name].astype("Int64")
    return out


def top_n(df: pd.DataFrame, n: int) -> pd.DataFrame:
    """
    Return top N rows.
    """
    if n <= 0:
        raise ValueError("n must be > 0")
    return df.head(n).reset_index(drop=True)
