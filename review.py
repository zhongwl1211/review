data = []
count = 0
with open('original.txt','r') as f:
   for line in f:
       data.append(line)
       count = count + 1
       if count % 1000 == 0:
       	     print(len(data)) 


print('檔案讀取完了','總共有',len(data),'筆資料') 

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('平均留言長度',sum_len/len(data))

#篩選留言
new = []
for d in data:
   if len(d) < 100:
      new.append(d)
print('一共有',len(new),'留言長度小於100')
print(new[0])

good=[]
for d in data:
   if 'good' in d:
      good.append(d)
print('一共有',len(good),'留言提到good')
print(good[0])