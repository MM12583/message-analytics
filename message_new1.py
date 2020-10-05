import time # 計時

def r_f(filename) :
    data = [] 
    with open (filename, 'r') as f :
        for line in f :
            data.append(line)
    return data

data = r_f('reviews.txt')
#print('共有', len(data), '筆資料')
#print(data[0])

# 文字記數
start_time = time.time() #start
wc = {} # word_count 字典
for d in data :
    words = d.strip().split() # 創作清單,用下一個迴圈讀每個字,split 預設值為空白鍵(不打可以避免空字串)
    for word in words : 
        if word in wc :
            wc[word] += 1 # 設變數 count 多此一舉,要再用sum
        else :
            wc[word] = 1  # ***用新增方式加入字典

for word in wc :
    if wc[word] >= 100000 : # 篩選大於100
        print(word, wc[word]) # 印出 wc[word] value值,即次數
end_time = time.time() # end 
print('花了', end_time - start_time, '秒')


while True : # 查詢
    word_search = input('輸入想查詢的字: ')
    if word_search == 'q' :
        break
    if word_search in wc :
        print(word_search, '總共出現', wc[word_search], '次') # 無法執行時會當掉. **wc[word_search] 找不到時
    else : 
        print('沒有', word_search, '這個字') # 避免當掉

print('感謝使用本查詢功能')