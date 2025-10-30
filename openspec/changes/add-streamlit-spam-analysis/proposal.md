## Why
以互動式應用快速進行垃圾郵件（spam）分析與示範，讓非技術使用者可視化探索資料、試用模型、並理解關鍵特徵；資料來源固定為本倉庫 `datasets/sms_spam_no_header.csv`，以確保可重現與教學穩定性，並以 Streamlit 建立端到端原型。

## What Changes
- 新增一個以 Streamlit 建置的 spam email 分析應用（本地執行）。
- 固定從本地檔案 `datasets/sms_spam_no_header.csv` 載入資料，提供資料瀏覽、分割、前處理與向量化。
- 內建基礎分類模型（優先：scikit-learn 如 LogisticRegression/LinearSVC；可替換 Hugging Face 文本分類管線）。
- 提供互動式推論（單筆輸入/批次測試）與評估（accuracy、precision、recall、F1、混淆矩陣）。
- 視覺化：類別分佈、最常見詞彙、關鍵詞雲（可選）、ROC/PR 曲線（若適用）。
- 產出可重現環境（requirements.txt）與 README（啟動說明）。

## Impact
- Affected specs: `specs/spam-analysis/spec.md`
- Affected code: 預計新增 `app/streamlit_app.py`、`app/data.py`、`app/model.py`、`requirements.txt`、`README.md`。
