import pandas as pd

people = pd.read_excel('./data/People.xlsx')

# 查看有多少行多少列
print(people.shape)

# 每一列的具体内容
print(people.columns)

# 默认是5行，也可以用people.head(3)表示看前3行
print(people.head())

print("================================================================================")

#看后5行,tail(3)表示后3行
print(people.tail())

#表格异常，有效数据第一行不是表格第一行,增加header参数，默认是0
people1 = pd.read_excel('./data/People1.xlsx', header=1)
print(people1.columns)

