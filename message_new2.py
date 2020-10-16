 # 讀取檔案
def r_f(filename) :
    import progressbar
    data = [] 
    count = 0
    bar = progressbar.ProgressBar(max_value = 1000000)
    with open (filename, 'r') as f :
        for line in f :
            data.append(line)
            count += 1
            bar.update(count)
            if count % 250000 == 0 : 
                print('已讀取' ,len(data), '筆資料')
    return data


# 列印字典 
def dictionary(data) :
    import time
    wc = {} 
    start_time = time.time()
    for d in data :
        words = d.strip().split()
        for word in words : 
            if word in wc :
                wc[word] += 1 
            else :
                wc[word] = 1  
    end_time = time.time()
    print('字典完成花了', end_time - start_time, '秒')
    return wc


# 篩選熱門字
def popular_word(wc) :
    popular = []
    for word in wc :
        if wc[word] >= 100000 : 
            popular.append(word) 
    print('共有', len(popular), '個字出現超過10萬次')
    return popular


# 查詢
def search() :
    while True : 
        word_search = input('輸入想查詢的字: ')
        if word_search == 'q' :
            break
        if word_search in wc :
            print(word_search, '總共出現', wc[word_search], '次') 
        else : 
            print('沒有', word_search, '這個字') 
    print('感謝使用本查詢功能')


def main() :
    data = r_f('reviews.txt')
    wc = dictionary(data)
    popular_word(wc)
    search()

main()