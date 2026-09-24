import pandas as pd
def load_data(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        print(f"Error loading data from {path}: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error


def report_missing_vals(df: pd.DataFrame) -> pd.DataFrame:
    missing = df.isna().sum()
    report = pd.DataFrame(
        {
            "column": missing.index,
            "missing values": missing.values,
            "percentage": (missing.values / len(df)) * 100,
        }
    )
    return report
