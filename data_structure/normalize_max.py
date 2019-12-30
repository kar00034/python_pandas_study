import pandas as pd
import numpy as np

df = pd.read_csv('./auto-mpg.csv',header=None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']

#horsepower 열의 누락데이터('?') 삭제하고 실수형으로 변환
df['horsepower'].replace('?',np.nan,inplace=True)
df.dropna(subset=['horsepower'],axis=0,inplace=True)
df['horsepower']=df['horsepower'].astype('float')

print("# horsepower 열의 통계 요약정보로 최대값(max)을 확인")
print(df.horsepower.describe(),'\n')

print("# horsepower 열의 최대값의 절대값으로 모든 데이터를 나눠서 저장")
df.horsepower = df.horsepower/abs(df.horsepower.max())

print(df.horsepower.head(),'\n',df.horsepower.describe())