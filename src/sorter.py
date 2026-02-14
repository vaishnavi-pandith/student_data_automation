from __future__ import annotations

import pandas as pd


def sort_dataframe(
    df: pd.DataFrame,
    sort_cols: list[str],
    ascending: list[bool] | bool = True,
    na_position: str = "last",
) -> pd.DataFrame:
    """
    Sort dataframe by one or multiple columns.
    """
    for c in sort_cols:
        if c not in df.columns:
            raise KeyError(f"Column '{c}' not found. Available: {list(df.columns)}")

    return df.sort_values(
        by=sort_cols,
        ascending=ascending,
        na_position=na_position,
        kind="mergesort",  # stable sort (good for multi-sort)
    ).reset_index(drop=True)
