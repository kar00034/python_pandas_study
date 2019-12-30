import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
print(df.head(),type(df),sep='\n')
print()

print("#데이터프레임에 숫자 10 더하기")
addition = df + 10
print(addition.head(), type(addition),sep='\n')