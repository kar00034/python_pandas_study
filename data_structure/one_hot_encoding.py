import pandas as pd
import numpy as np
from sklearn import preprocessing

df = pd.read_csv('./auto-mpg.csv',header=None)
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

df['horsepower'].replace('?',np.nan,inplace=True)
df.dropna(subset=['horsepower'],axis=0,inplace=True)
df['horsepower']=df['horsepower'].astype('float')

count,bin_dividers=np.histogram(df['horsepower'],bins=3)

bin_names=['저출력','보통출력','고출력']
df['hp_bin']=pd.cut(x=df['horsepower'],bins=bin_dividers,labels=bin_names,include_lowest=True)

label_encoder = preprocessing.LabelEncoder()
onehot_encoder = preprocessing.OneHotEncoder(categories='auto')

print("# label encoder로 문자열 범주를 숫자형 범주로 변환")
onehot_labeled = label_encoder.fit_transform(df['hp_bin'].head(15))
print(onehot_labeled,'\n',type(onehot_labeled),'\n')

print("# 2차원 행렬로 형태 변경")
onehot_reshaped = onehot_labeled.reshape(len(onehot_labeled),1)
print(onehot_reshaped,'\n',type(onehot_reshaped),'\n')

print("# 희소행렬로 변환")
onehot_fitted = onehot_encoder.fit_transform(onehot_reshaped)
print(onehot_fitted,'\n',type(onehot_fitted))