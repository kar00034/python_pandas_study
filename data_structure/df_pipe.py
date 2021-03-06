import seaborn as sns

print("# titanic 데이터셋에서 age,fare 2개열을 선택하여 데이터프레임 만들기")
titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age','fare']]
print(df.head())
print()

def missing_value(x):
    return x.isnull()

def missing_count(x):
    return missing_value(x).sum()

def total_number_missing(x):
    return missing_count(x).sum()

print("각 열의 NaN찾기 - 데이터프레임 전달하면 데이터프레임을 반환")
result_df = df.pipe(missing_value)
print(result_df.head(),type(result_df),sep = '\n')
print()

print("# 각 열의 NaN 개수 반환 - 데이터프레임 전달하면 시리즈 반환")
result_series = df.pipe(missing_count)
print(result_series,type(result_series),sep='\n')
print()

print("# 데이터프레임의 총 NaN 개수 - 데이터프레임 전달하면 값을 반환")
result_value = df.pipe(total_number_missing)
print(result_value,type(result_value),sep='\n')