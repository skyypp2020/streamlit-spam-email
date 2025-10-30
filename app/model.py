from typing import Tuple, List
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_recall_fscore_support


TEXT_COL = "text"
LABEL_COL = "label"


def build_pipeline(ngram_max: int = 1, c_value: float = 1.0) -> Pipeline:
    vectorizer = TfidfVectorizer(ngram_range=(1, ngram_max), stop_words='english')
    clf = LogisticRegression(max_iter=200, C=c_value, n_jobs=None)
    return Pipeline([
        ("tfidf", vectorizer),
        ("clf", clf),
    ])


def train_and_evaluate(train_df: pd.DataFrame,
                       test_df: pd.DataFrame,
                       ngram_max: int = 1,
                       c_value: float = 1.0) -> Tuple[Pipeline, dict]:
    model = build_pipeline(ngram_max, c_value)
    model.fit(train_df[TEXT_COL], train_df[LABEL_COL])

    preds = model.predict(test_df[TEXT_COL])
    acc = accuracy_score(test_df[LABEL_COL], preds)
    precision, recall, f1, _ = precision_recall_fscore_support(
        test_df[LABEL_COL], preds, average='weighted', zero_division=0
    )
    cm = confusion_matrix(test_df[LABEL_COL], preds).tolist()

    report = {
        "accuracy": acc,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "confusion_matrix": cm,
        "labels": sorted(test_df[LABEL_COL].unique().tolist())
    }
    return model, report


def predict_single(model: Pipeline, text: str) -> Tuple[str, float]:
    proba = None
    if hasattr(model.named_steps.get("clf"), "predict_proba"):
        probs = model.predict_proba([text])[0]
        idx = int(np.argmax(probs))
        label = model.classes_[idx]
        proba = float(probs[idx])
    else:
        label = model.predict([text])[0]
        proba = 1.0
    return str(label), float(proba)


def predict_batch(model: Pipeline, texts: List[str]) -> List[Tuple[str, float]]:
    results = []
    if hasattr(model.named_steps.get("clf"), "predict_proba"):
        probs_all = model.predict_proba(texts)
        for i, probs in enumerate(probs_all):
            idx = int(np.argmax(probs))
            label = model.classes_[idx]
            results.append((str(label), float(probs[idx])))
    else:
        labels = model.predict(texts)
        for label in labels:
            results.append((str(label), 1.0))
    return results
