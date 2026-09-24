import pandas as pd
from itertools import permutations

def fd_violations(df: pd.DataFrame, lhs, rhs: str) -> int:
    """Number of distinct LHS values that map to more than one RHS value."""
    counts = df.groupby(lhs, dropna=False)[rhs].nunique(dropna=False)
    return int((counts > 1).sum())


from itertools import permutations
#lhs->rhs

def check_all_fds(df: pd.DataFrame) -> pd.DataFrame:
    columns = list(df.columns)
    results = []

    for lhs, rhs in permutations(columns, 2):
        violations = fd_violations(df, lhs, rhs)
        results.append(
            {
                "Determinant": lhs,
                "Dependent": rhs,
                "Violations": violations,
                "Holds": violations == 0,
            }
        )

    return pd.DataFrame(results, columns=["Determinant", "Dependent", "Violations", "Holds"])