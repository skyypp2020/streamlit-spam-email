## 1. Implementation
- [ ] 1.1 建立專案結構與 requirements.txt（streamlit、scikit-learn、pandas、numpy、plotly、wordcloud 可選）
- [ ] 1.2 資料載入模組：從本地 `datasets/sms_spam_no_header.csv` 載入、資料清理與分割
- [ ] 1.3 特徵工程：文字正規化、TF-IDF 向量化（或 HF pipeline tokenization）
- [ ] 1.4 建立與訓練基礎模型（LogisticRegression/LinearSVC）與儲存/載入
- [ ] 1.5 Streamlit 介面：資料瀏覽、統計圖表、互動式推論（單筆/批次）
- [ ] 1.5.1 單筆推論輸入框新增兩個按鈕：「Use spam example」/「Use ham example」
- [ ] 1.6 評估指標與視覺化（accuracy、precision、recall、F1、混淆矩陣、ROC/PR）
- [ ] 1.7 文件：README（啟動方式、資料來源、授權）、範例截圖
- [ ] 1.8 QA：以小樣本驗證；必要時抽換資料集；調整預設參數
- [ ] 1.9 打包啟動腳本（`streamlit run app/streamlit_app.py`）與簡單測試腳本

## 2. Validation
- [ ] 2.1 本地可啟動、互動正常
- [ ] 2.2 指標計算與可視化正確
- [ ] 2.3 最低執行資源說明與效能檢查

## 3. Release
- [ ] 3.1 初次發布說明與變更記錄
- [ ] 3.2 （可選）提供 Dockerfile 與執行指令
