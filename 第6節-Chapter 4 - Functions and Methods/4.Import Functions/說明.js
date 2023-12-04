// ❗ Import Functioins 
//  之前有用過 import math、form sys import argv(avguments)
// 
//  像是有些很實用的 function 或是別人寫好的 就需要使用 import
// 
// 
// 一些很常使用的 common modules
// 1. requests 網頁請求 HTTP
// 2. bs4(for web scraping) 網路爬蟲
// 3. numpy
// 4. pandas
// 5. matplotlib
// 6. seaborn(3~6 都是資料視覺化data visualization)
// 7. random
// 8. sklearn
// 9. tensorflow(7~9 人工智能machine learning, deep learning)
// 10. 


// 為什麼 要有 import 為何不一開始就在 function
// 1. 因為如果預設就包含 這樣跑文件的時間就會增加
// 2. it keeps the global namespace(就是原先預設好的東西) clean and allows functionality to be grouped logically into modules
// 3. 不同的 modules 可能會有相同的名稱，用了 import 就可以決定要使用哪一個 Different modules can have identically-named functions without
//      clashes(file and socket class would probably both have open and close functions, for example). it makes sure we don't mess up the names