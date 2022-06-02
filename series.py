import pandas as pd
# 在pandas里面实现行、列、单元格
s1 = pd.Series([1, 2, 3], index=[1, 2, 3], name='A')
s2 = pd.Series([10, 20, 30], index=[1, 2, 3], name='B')
s3 = pd.Series([100, 200, 300], index=[1, 2, 3], name='C')

df = pd.DataFrame({s1.name:s1, s2.name:s2, s3.name:s3})
print(df)
# 输出结果：
#    A   B    C
# 1  1  10  100
# 2  2  20  200
# 3  3  30  300

print("==========================================")
df = pd.DataFrame([s1,s2,s3])
print(df)
# 输出结果
#      1    2    3
# A    1    2    3
# B   10   20   30
# C  100  200  300