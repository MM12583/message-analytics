data = [] # 建立空清單
data_50 = []
count = 0 # ***數資料目前次數
with open ('reviews.txt', 'r') as f :
    for line in f :
            data.append(line) # 將line變數逐一裝入data 
            count += 1
            if len(line) <= 50 :  # 篩選留言長度小於50
                data_50.append(line)
            if count % 100000 == 0 : # 求餘數 % 整除 100000
                print('以讀取' ,len(data), '筆資料')

print('共有', len(data), '筆資料') # len 印出長度
print('共有', len(data_50), '筆資料長度小於50') 

# 算平均留言長度
sum_len = 0 # sum 算總和
for d in data :
    sum_len += len(d) #sum_len = sum_len + len(d)
    sum_average = round(sum_len / len(data))
print('平均留言長度為', sum_average)
