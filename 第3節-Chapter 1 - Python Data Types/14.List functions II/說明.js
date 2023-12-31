// ❗ Built-in(內建) Methods(方法) for List II
// 
// 
// 上節講的
// 1. insert() - 插入的意思
// 2. remove() - 移除某一個特定的 element
// 3. clear() - 清空 list
// 4. sort() - 排序的意思 可以按照 字母大小寫 也是 資料中很重要的演算法
// 5. reverse() - 反轉的意思

// 這節講的
// 6. append() - 將東西加入 list 的最後面
// 7. pop() - 將 list 最後面的 emelemt 移除
// 8. copy() - 這個牽扯到了記憶體問題，會使用這個是因為 list 是 copy by reference 但我只想要 copy by value 那這樣就可以使用此 Methods
//              copy by value(值)                                               
//              a = 10  a 目前指向記憶體的某個空間，這個空間目前裝著 10 
//              b = a   這時會發生 copy by value，等號右邊的 a 是 10，b 就會找到記憶體某個空間將 a 的值 copy 到他自己的空間       
//-------------------------------------------------------------------------------------------------------------------------------
//              copy by reference(指電腦的memory)RAM 就是記憶體的位置
//              x = [1, 2, 3]   x 目前指向記憶體 3 格位置，分別為 1, 2, 3
//              y = x           這時會發生 copy by reference，就會將 x 的位置 指向給 y，但是空間的位置是一樣的
//              y[0] = 15       這時因為 x 指向 y，y 的改變，一樣會改變到 x
// 9. 
// 10. 