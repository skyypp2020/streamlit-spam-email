# Streamlit Spam Analysis App

Demo Site: https://app-spam-email-d4cf7jtshc9gkq5ovdefbs.streamlit.app/

This app implements the OpenSpec spec at `openspec/specs/spam-analysis/spec.md`.

## Quickstart

1) Install dependencies
```bash
pip install -r requirements.txt
```

2) Prepare dataset
- Place `datasets/sms_spam_no_header.csv` in the repo (two columns: label,text without header)

3) Run app
```bash
streamlit run app/streamlit_app.py
```

## Features
- Dataset load from `datasets/sms_spam_no_header.csv`
- Train TF-IDF + LogisticRegression
- Single text inference with quick-fill buttons: "Use spam example" / "Use ham example"
- Batch inference from CSV
- Confusion matrix visualization

## CRISP-DM（專案方法論）

### 1. Business Understanding（商業理解）
- 目標：提供互動式垃圾郵件偵測示範，協助教學與快速驗證文本分類流程。
- 成果：可視化資料、訓練模型、即時推論（含範例按鈕），並呈現評估指標。

### 2. Data Understanding（資料理解）
- 資料來源：`datasets/sms_spam_no_header.csv`（無表頭，兩欄：label、text）。
- 初探：在 Streamlit 的 Data 分頁可檢視樣本數、類別分佈、隨機樣本。
- 注意：label 與 text 會在載入時做基本清理（去空白、小寫化）。

### 3. Data Preparation（資料準備）
- 檔案載入與欄位命名：見 `app/data.py`，自動指派 `label`、`text` 欄位。
- 資料切分：`train_test_split`（預設 test_size=0.2、stratify by label）。
- 文字正規化與向量化：`TfidfVectorizer`（可調 n-gram 範圍）。

### 4. Modeling（建模）
- 預設模型：TF-IDF + LogisticRegression（可調 C 值與 n-gram）。
- 程式位置：`app/model.py`（建置管線、訓練、單筆/批次推論）。
- 訓練入口：Streamlit 的 Train 分頁；完成後儲存在記憶體的 session state。

### 5. Evaluation（評估）
- 指標：accuracy、precision、recall、F1。
- 視覺化：Confusion Matrix（Visualization 分頁）。
- 互動驗證：Inference 分頁可輸入文字，或使用「Use spam example／Use ham example」隨機抽樣示例並顯示對應機率。

### 6. Deployment（部署）
- 本地啟動：`streamlit run app/streamlit_app.py`（或 `python -m streamlit run app/streamlit_app.py`）。
- 依賴安裝：`pip install -r requirements.txt`。
- 發佈建議：可上傳到雲端機器/教學環境，以本地直跑為主（本版不提供 Docker 與 HF pipeline）。
