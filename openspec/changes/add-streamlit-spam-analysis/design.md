## Context
- 本變更提案新增一個使用 Streamlit 的互動式 spam email 分析應用，資料固定來自本倉庫 `datasets/sms_spam_no_header.csv`，以利穩定教學與重現。
- 目標：教學友善、可快速上手、可離線本地執行；避免過度工程化。
- 依賴：`streamlit`、`scikit-learn`、`pandas`、`numpy`、`plotly`（視覺化）、`wordcloud`（可選）。

## Goals / Non-Goals
- Goals:
  - 提供互動式資料探索、模型訓練與推論介面
  - 從本地 `datasets/sms_spam_no_header.csv` 載入資料
  - 以簡單可理解的傳統 ML 模型為預設（可替換）
- Non-Goals:
  - 生產級 MLOps/模型部署
  - 多租戶/權限控管
  - 大規模資料/分散式訓練
  - Docker 化（課堂部署以本地直跑為主）
  - 內建中文資料集與繁中介面預設（可於後續版本考量）
  - 內建 Hugging Face 文本分類管線切換選項（先聚焦 TF-IDF+LR）

## Decisions
- 預設模型選擇：TF-IDF + LogisticRegression（可選 LinearSVC），平衡可解釋性與效果。
- 資料集：固定檔案 `datasets/sms_spam_no_header.csv`（無表頭，需在 `data.py` 明確指定欄位名稱）。
- 分層：`app/data.py`（資料載入與前處理）、`app/model.py`（訓練/評估/儲存）、`app/streamlit_app.py`（UI）。
- 評估：accuracy、precision、recall、F1，並提供混淆矩陣與（可選）ROC/PR 圖。
- 互動：單筆輸入、批次測試上傳（CSV/TXT），顯示分類結果與信心分數。
 - 互動：單筆輸入、批次測試上傳（CSV/TXT），顯示分類結果與信心分數；單筆輸入提供兩個一鍵填入按鈕（「Use spam example」/「Use ham example」），便於示範。
 - 範圍限制（本版不納入）：Docker、中文資料集/繁中介面預設、Hugging Face pipeline 切換。

## Risks / Trade-offs
- 風險：資料集授權/可用性差異 → 指定至少一個穩定資料集，並在 README 註明。
- 風險：中文資料支援 → 初版以英文資料集示範，README 提供替換指引。
- 風險：模型效果預期 → 提供參數面板（ngram、正規化、C 值）供使用者微調。
- 取捨：簡潔優先於最強效果；維持 <1000 行程式碼與單機易用。

## Migration Plan
1) 新增目錄與程式檔，撰寫 README 與 requirements。
2) 小樣本驗證與互動測試。
3) 文件補強與螢幕截圖。

## Open Questions
（本版無）
