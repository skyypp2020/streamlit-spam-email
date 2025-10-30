import os
import pandas as pd
from typing import Tuple
from sklearn.model_selection import train_test_split

DEFAULT_DATA_PATH = os.path.join("datasets", "sms_spam_no_header.csv")


def load_dataset(csv_path: str = DEFAULT_DATA_PATH,
                 text_col: str = "text",
                 label_col: str = "label",
                 test_size: float = 0.2,
                 random_state: int = 42) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Load dataset without header from csv_path and assign column names.
    Expects two columns: label, text (no header in file).
    Returns (train_df, test_df).
    """
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Dataset file not found: {csv_path}")

    df = pd.read_csv(csv_path, header=None, names=[label_col, text_col])

    # Basic cleaning
    df[text_col] = df[text_col].astype(str).str.strip()
    df[label_col] = df[label_col].astype(str).str.strip().str.lower()

    train_df, test_df = train_test_split(
        df, test_size=test_size, random_state=random_state, stratify=df[label_col]
    )
    return train_df.reset_index(drop=True), test_df.reset_index(drop=True)
