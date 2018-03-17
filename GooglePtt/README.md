# GooglePtt
## 使用 Google 搜尋對 PTT 進行關鍵字爬蟲

### google_ptt.py

主要的搜尋 & 爬蟲程式碼

|參數|說明|範例|
|:---:|:---|:---|
|-f|設定檔案存放的位置|`-f "D:/Hello/"` 會在 "D:/Hello/" 下建立一個 PTT 資料夾進行工作|
|-w|設定搜尋關鍵字|`-w 棒球 籃球` 將會對「棒球」和「籃球」兩個關鍵字分別進行搜尋|
|-t|設定時間範圍，h d w m y分別代表時、日、週、月、年|`-t w` 表示搜尋過去一週|