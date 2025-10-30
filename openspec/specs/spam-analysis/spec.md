### Requirement: Streamlit Spam Analysis App
系統 SHALL 提供一個以 Streamlit 建置的互動式垃圾郵件分析應用，資料固定來自 `datasets/sms_spam_no_header.csv`，允許使用者瀏覽資料統計、訓練/載入模型、進行單筆與批次推論，並檢視評估指標與可視化結果。

#### Scenario: App startup
- **WHEN** 使用者執行 `streamlit run app/streamlit_app.py`
- **THEN** 顯示應用首頁並提供資料載入、模型面板與評估區塊

#### Scenario: Dataset load
- **WHEN** 系統讀取本地檔案 `datasets/sms_spam_no_header.csv`
- **THEN** 系統 MUST 正確解析（無表頭，採指定欄位名）並載入資料，顯示基本統計（樣本數、類別分佈）

#### Scenario: Train model
- **WHEN** 使用者於訓練面板設定參數並觸發訓練
- **THEN** 系統 SHALL 使用 TF-IDF 與 LogisticRegression（預設）完成訓練並回報指標

#### Scenario: Inference single text
- **WHEN** 使用者於輸入框輸入一段文字並送出
- **THEN** 系統 MUST 回傳 spam/ham 預測與信心分數

#### Scenario: Quick-fill buttons for single text
- **WHEN** 使用者點擊「Use spam example」按鈕
- **THEN** 系統 SHALL 將預設的垃圾郵件示例文字填入輸入框，使用者可直接送出以獲得預測

- **WHEN** 使用者點擊「Use ham example」按鈕
- **THEN** 系統 SHALL 將預設的正常郵件示例文字填入輸入框，使用者可直接送出以獲得預測

#### Scenario: Inference batch
- **WHEN** 使用者上傳含文字欄位之 CSV 檔並選擇欄位
- **THEN** 系統 SHALL 對每列輸入產出預測並提供可下載結果

#### Scenario: Visualization
- **WHEN** 使用者開啟視覺化分頁
- **THEN** 系統 SHALL 顯示類別分佈、最常見詞彙，並可選擇顯示混淆矩陣與 ROC/PR（若適用）
