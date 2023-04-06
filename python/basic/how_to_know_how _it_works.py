

a = [1,2,3,4,5]
print("변경 전 a :",a)
b = a[0]
print('b의 타입 :', type(b))  # 표시되는 int class는 immutable(변경 불가능)입니다.(해당 클래스를 찾아보면 def __hash__ 가 정의 되어있음)
b = 10
print("b를 변경 후 a :",a)

print()
print()

print(list())
c = [[1,2],[2,3],[4,5]]
print("변경 전 c :",c)
d = c[0]
print('d의 타입 :', type(d)) # 표시되는 list class는 mutable(변경 가능)입니다.(해당 클래스를 찾아보면 def __hash__ 가 정의 되어 있지 않음 )
d[0] = 2
print("d를 변경 후 c :",c)


print()
print()


import pandas as pd
import numpy as np

arry = np.array([1,2,3])

print(type(arry))
df = pd.DataFrame({'name':['a','b','c'], 'age':[1,2,3]})
print("변경 전 df :",df)

pd.Series()
s = df['age']
print(id(df['age']))
print(id(s))
print('s의 타입 :', type(s))

s[0] = 10

# s.loc[0] = 10
print("변경 후 df :",df)
