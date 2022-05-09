import pandas as pd
from collections import defaultdict

# 读排表
data = pd.read_csv('11.csv', encoding='utf-8')

# 获取谷名 作为value
firstline = list(data.columns.values)
goods = firstline[1:]

# 按行遍历排表，第一列作为key，后面的作为value的值  用defaultdict
# 创建pair=[('TSUKI','日1'),('TSUKI','及1')……]
# 放在元组里,然后加到pair里，pair再到dict里

# 元组list
pair = []
for index, row in data.iterrows():  # 遍历每一行
    for good in goods:  # 获得每个谷名的情况
        if str(row[good]) != 'nan':
            str1 = data.iloc[index, 0]
            str2 = good + str(row[good])
            tmptup = (str1, str2)
            pair.append(tmptup)
# 字典
pb = defaultdict(list)
for key, value in pair:
    pb[key].append(value)
print(pb)

# print(index,type(row),row[good])


# print(data)
