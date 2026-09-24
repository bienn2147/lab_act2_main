import pandas as pd


def check_id_uniqueness(df: pd.DataFrame) -> pd.DataFrame:
    ''''''Check uniqueness of every column whose name contains 'ID'.

    Columns are matched if their name contains 'ID' (case-insensitive). A
    column is considered unique when it has no duplicate non-null values.
    'n duplicates' counts the number of extra occurrences beyond the first,
    i.e. total rows minus the number of distinct non-null values.

    Returns a DataFrame with columns: 'column name', 'unique', 'n duplicates'.
    ''''''
    id_cols = [col for col in df.columns if 'id' in str(col).lower()]

    results = []
    for col in id_cols:
        non_null = df[col].dropna()
        n_duplicates = int(non_null.duplicated().sum())
        results.append(
            {
                'column name': col,
                'unique': n_duplicates == 0,
                'n duplicates': n_duplicates,
            }
        )

    return pd.DataFrame(
        results, columns=['column name', 'unique', 'n duplicates']
    )
