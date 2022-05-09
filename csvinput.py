import pandas as pd
from collections import defaultdict

#读排表
data=pd.read_csv('test.csv',encoding='utf-8')

#获取谷名 作为value
firstline =list(data.columns.values)
goods=firstline[1:]

#按行遍历排表 第一列作为key 后面的作为value的值 用defaultdict
#创建pair=[('tsuki','日1'),('tsuki','及1')……]
#放在元组里，然后加到pair里，pair再到dict里

#元组list
pair=[]
for index,row in data.iterrows():
    for good in goods:
        if str(row[good])!='nan':
            cn=data.iloc[index,0]
            goodnm=good+str(row[good])
            tmptup=(cn,goodnm)
            pair.append(tmptup)

#字典
pb=defaultdict(list)
for key,value in pair:
    pb[key].append(value)
print(pb)