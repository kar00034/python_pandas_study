import pandas as pd
import numpy as np

df = pd.read_csv('./auto-mpg.csv',header=None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']

#디스플레이 설정
pd.set_option('display.max_columns',len(df.columns))
pd.set_option('display.max_colwidth',int(df['name'].apply(len).max()))
pd.set_option('display.unicode.east_asian_width',True)
pd.set_option('display.width',600)

print('df.head()','\n',df.head(),'\n')

#horsepower 열의 누락 데이터('?')를 삭제하고 실수형으로 변환
df['horsepower'].replace('?',np.nan,inplace=True)
df.dropna(subset=['horsepower'],axis=0,inplace=True)
df['horsepower'] = df['horsepower'].astype('float')

print("# np.histogram으로 3개의 bin으로 나누는 경계 값의 리스트 구하기")
count, bin_dividers = np.histogram(df['horsepower'],bins=3)

bin_names=['저출력','보통출력','고출력']

df['hp_bin']=pd.cut(x=df['horsepower'], bins=bin_dividers,labels=bin_names, include_lowest=True)

print("# hp_bin 열의 범주형 데이터를 더미 변수로 변환")
horsepower_dummies=pd.get_dummies(df['hp_bin'])
print(horsepower_dummies.head(15),'\n')

print("df[['horsepower','hp_bin'.head]](15)",'\n',df[['horsepower','hp_bin']].head(15),'\n')