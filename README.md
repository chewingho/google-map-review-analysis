# google-map-reviews-analysis
爬取知名飲料店的google map評論，進行資料視覺化分析與評論內容(comment)文字分析
## Description
爬取嘉義知名飲料店-源興御香屋google map時間由近到遠4000筆資料，  
欄位包含使用者名稱(username)、時間(time)、評論內容(comment)、評分數(star)  
並進行資料視覺化分析評分數、評論內容可信度、時間與評分數  
與評論內容的文字分析，分析各評分數的關鍵字。  

## Analysis  

[御香屋google map爬蟲](https://github.com/chewingho/google-map-reviews-analysis/blob/master/%E5%BE%A1%E9%A6%99%E5%B1%8Bgoogle%20map%E7%88%AC%E8%9F%B2.ipynb)  
1. 4000筆各star(1~5)的數量  
2. 4000筆各star(1~5)的comment是否為None，或是有提供敘述  
3. 10個月內每月star分析 
##
[御香屋google map評價文字分析](https://github.com/chewingho/google-map-reviews-analysis/blob/master/%E5%BE%A1%E9%A6%99%E5%B1%8Bgoogle%20map%E8%A9%95%E5%83%B9%E6%96%87%E5%AD%97%E5%88%86%E6%9E%90.ipynb)  
1. 4000筆前20個關鍵字  
2. 4000筆各star前20個關鍵字，並繪製成文字雲  
