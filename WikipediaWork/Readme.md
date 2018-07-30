# Wikipedia Project

## Data Description
+ interlang_links_org: 中文詞條對應其他語言的詞條檔案
+ interlang_links_zh_en: 只留下中文與英文詞條對應關係
+ zhwiki_main_tw: 繁體中文的 Dump XML
+ zhwiki_preserve_tw: 只留下每個 Page 的首段章節
+ zhwiki_sub_org: 從 zhwiki_preserve_tw 取出前十個檔案的小集合
+ zhwiki_sub_plain: 將 wikitext 語法轉換成純文字的結果
+ zhwiki_sub_seg: 將純文字進行長詞優先斷詞後的結果
+ zhwiki_sub_seg_fix: 因為 page 沒有正確加上標籤，修正後的版本
+ zhwiki_sub_seg_fix_small: 每個 pageset 只留下 8 個 page 的更小集合

## Python Code
+ preserve_truncate.py: 將首段章節取出
+ preprocesser.py: 處理 Wikitext