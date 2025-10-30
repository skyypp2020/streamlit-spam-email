import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from app.data import load_dataset, DEFAULT_DATA_PATH
from app.model import train_and_evaluate, predict_single, predict_batch, TEXT_COL, LABEL_COL

st.set_page_config(page_title="Spam Analysis", layout="wide")
st.title("Streamlit Spam Analysis App")

# Sidebar config
st.sidebar.header("Configuration")
data_path = st.sidebar.text_input("Dataset path", value=DEFAULT_DATA_PATH)
ngram_max = st.sidebar.slider("N-gram max", 1, 3, 1)
c_value = st.sidebar.slider("LogReg C", 0.1, 3.0, 1.0, step=0.1)

@st.cache_data(show_spinner=False)
def cached_load(path: str):
    return load_dataset(path)

# Load dataset
try:
    train_df, test_df = cached_load(data_path)
except Exception as e:
    st.error(f"Failed to load dataset: {e}")
    st.stop()

full_df = pd.concat([train_df, test_df], ignore_index=True)

# Session state for model
if "model" not in st.session_state:
    st.session_state.model = None
if "report" not in st.session_state:
    st.session_state.report = None

# Tabs
tab_data, tab_train, tab_infer, tab_viz = st.tabs(["Data", "Train", "Inference", "Visualization"])

with tab_data:
    st.subheader("Dataset Overview")
    st.write(f"Train size: {len(train_df)} | Test size: {len(test_df)}")
    st.write("Class distribution (train):")
    st.dataframe(train_df[LABEL_COL].value_counts().rename_axis("label").reset_index(name="count"))
    st.write("Sample rows:")
    st.dataframe(train_df.sample(min(10, len(train_df))))

with tab_train:
    st.subheader("Train Model")
    if st.button("Train"):
        with st.spinner("Training..."):
            model, report = train_and_evaluate(train_df, test_df, ngram_max=ngram_max, c_value=c_value)
            st.session_state.model = model
            st.session_state.report = report
        st.success("Training finished")
        st.json(st.session_state.report)
    if st.session_state.report:
        st.metric("Accuracy", f"{st.session_state.report['accuracy']:.3f}")

with tab_infer:
    st.subheader("Single Text Inference")

    def sample_text_by_label(df: pd.DataFrame, target_label: str) -> str:
        subset = df[df[LABEL_COL] == target_label]
        if subset.empty:
            return ""
        return subset.sample(1, random_state=np.random.randint(0, 10_000))[TEXT_COL].iloc[0]

    # Quick-fill examples
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("Use spam example"):
            st.session_state.example_text = sample_text_by_label(full_df, "spam")
            st.session_state.target_label = "spam"
    with col_b:
        if st.button("Use ham example"):
            st.session_state.example_text = sample_text_by_label(full_df, "ham")
            st.session_state.target_label = "ham"

    default_text = st.session_state.get("example_text", "")
    user_text = st.text_area("Enter text", value=default_text, height=120)

    if st.button("Predict"):
        if st.session_state.model is None:
            st.warning("Please train the model first.")
        else:
            # Compute probabilities if available
            model = st.session_state.model
            target = st.session_state.get("target_label")
            if hasattr(model.named_steps.get("clf"), "predict_proba"):
                probs = model.predict_proba([user_text])[0]
                classes = list(model.classes_)
                # Map to spam/ham if available
                prob_map = {cls: float(probs[idx]) for idx, cls in enumerate(classes)}
                if target in ("spam", "ham") and target in prob_map:
                    st.success(f"{target} probability = {prob_map[target]:.4f}")
                else:
                    # Fallback show predicted label and top prob
                    label, score = predict_single(model, user_text)
                    st.info(f"Prediction: {label} | confidence: {score:.3f}")
            else:
                # Fallback if classifier has no probas
                label, score = predict_single(model, user_text)
                st.info(f"Prediction: {label} | confidence: {score:.3f}")

    st.divider()
    st.subheader("Batch Inference")
    uploaded = st.file_uploader("Upload CSV with a text column", type=["csv"]) 
    text_column_name = st.text_input("Text column name", value=TEXT_COL)
    if uploaded and st.session_state.model is not None:
        df_up = pd.read_csv(uploaded)
        if text_column_name not in df_up.columns:
            st.error(f"Column '{text_column_name}' not in uploaded CSV.")
        else:
            preds = predict_batch(st.session_state.model, df_up[text_column_name].astype(str).tolist())
            df_up["pred_label"] = [p[0] for p in preds]
            df_up["pred_score"] = [p[1] for p in preds]
            st.dataframe(df_up.head(50))
            st.download_button("Download predictions", df_up.to_csv(index=False), file_name="predictions.csv")

with tab_viz:
    st.subheader("Visualizations")
    if st.session_state.report:
        labels = st.session_state.report["labels"]
        cm = st.session_state.report["confusion_matrix"]
        cm_df = pd.DataFrame(cm, index=labels, columns=labels)
        fig = px.imshow(cm_df, text_auto=True, color_continuous_scale="Blues",
                        labels=dict(x="Predicted", y="True", color="Count"))
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Train a model to see confusion matrix.")
