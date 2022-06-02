import pandas as pd

df = pd.DataFrame({'id':[1, 2, 3], 'name':['Tom','Jane','Nick']})
print(df)
# 输出结果如下：
#    id  name
# 0   1   Tom
# 1   2  Jane
# 2   3  Nick

'''自定义index'''
df = df.set_index('id')
print(df)
# 输出结果如下：（存入excel正常）
#     name
# id
# 1    Tom
# 2   Jane
# 3   Nick
'''写入到excel中'''
df.to_excel('./data/output.xlsx')

'''读excel里面的内容'''
df = pd.read_excel('./data/output.xlsx')
print(df)
# 输出结果如下：
#    id  name
# 0   1   Tom
# 1   2  Jane
# 2   3  Nick


