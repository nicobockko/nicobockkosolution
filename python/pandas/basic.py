import pandas as pd

pd.Series
df = pd.read_excel('t.xlsx') #타이타닉 데이터 
df = df.iloc[:, 1:]
print(df.columns)

# ##하나의 열을 가져 오고 싶을 때
### print(df[0])  #에러발생 - 열을 읽을땐 열 이름을 적어줘야함
# print(df['age'].head(3))
# print(df.loc[:,'age'].head(3))
# print(df.iloc[:,3].head(3))
# ### print(df.iloc[:,'age']) #에러발생 - iloc의 의미는 integer location 이라, 숫자만 가능!
# print(type(df['age']),type(df.loc[:,'age']),type(df.iloc[:,3].head(3)))


# ##여러 개의 열을 가져 오고 싶을 때
### print(df[[0,1]])  #에러발생 - 열을 읽을땐 열 이름을 적어줘야함
# print(df[['age','sex']].head(3))
# print(df.loc[:,['age','sex']].head(3))
# print(type(df[['age','sex']]),type(df.loc[:,['age','sex']]))

# ##하나의 행을 가져 오고 싶을 때
# print(df.loc[0].head(3))
# print(df.iloc[0].head(3))
# print(type(df.loc[0]),type(df.iloc[0]))

# print(df.loc[0,:].head(3))
# print(df.iloc[0,:].head(3))
# print(type(df.loc[0,:]),type(df.iloc[0,:]))
#
# ##여러개의 행을 가져 오고 싶을 때
# print(df.loc[[2,6]].head(3))
# print(df.iloc[[2,6]].head(3))
# print(type(df.loc[[2,6]]),type(df.iloc[[2,6]]))

# print(df.loc[[2,6],:].head(3))
# print(df.iloc[[2,6],:].head(3))
# print(type(df.loc[[2,6],:]),type(df.iloc[[2,6],:]))


##하나의 값을 가져오고 싶을 때
print(df['age'][6])
print(df.loc[6]['age'])
print(df.loc[6, 'age'])
print(df.iloc[6][4])
print(df.iloc[6, 4])
print(df.at[6, 'age'])
print(df.iat[6, 4])

# # ##하나의 값을 변경하고 싶을 때
#
# df['age'][6] = 73  #경고메시지 -  2중 column 일 수 있기 때문,
# # df.loc[6]['age'] = 83  #불가
# df.loc[6,'age'] = 93
# # df.iloc[6][4] = 103 #불가
# df.iloc[6,4]  = 113
# df.at[6,'age'] = 123
# df.iat[6,4] = 133

# print(df['age'][6])
# print(df.loc[6]['age'])
# print(df.loc[6,'age'])
# print(df.iloc[6][4])
# print(df.iloc[6,4])
# print(df.at[6,'age'])
# print(df.iat[6,4])


print(df['age'][:10] > 23)
print(type(df['age'][:10] > 23))

df_sample = df[:][:5]
print(df_sample)

print(df_sample[[True, False, False, True, True]])
print(df_sample[df_sample['age'] > 23])

print(df_sample.loc[[True, False, False, True, True]]['age'])
print(df_sample.loc[[True, False, False, True, True], :])

print(df_sample.loc[df_sample['age'] > 23])
print(df_sample.loc[df_sample['age'] > 23, :])

# print(type(df.describe()))
# print(df.describe().columns)
# print(df.describe().index)


print(df.dtypes)

print(df.groupby('pclass'))
print(type(df.groupby('pclass')))

print(df.groupby('pclass').mean(numeric_only=True))
print(df.groupby('pclass').mean())
print(type(df.groupby('pclass').mean(numeric_only=True)))

print(df.groupby('pclass')['age'].mean())
print(df.groupby('pclass').mean(numeric_only=True)['age'])
