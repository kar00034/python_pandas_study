import seaborn as sns
import pandas as pd
import numpy as np

from data_structure.set_dis import set_dis

titanic = sns.load_dataset('titanic')
print(titanic,'\n')

print("#나이가 10대인 승객만")
mask1 = (titanic.age >=10) & (titanic.age <20)
df_teenage = titanic.loc[mask1]
print(df_teenage.head(),'\n')

print("#나이가 10세 미만이고 여성인 승객만")
mask2 = (titanic.age < 10) & (titanic.sex == 'female')
df_female_under10 = titanic.loc[mask2]
print(df_female_under10.head(),'\n')

print("#나이가 10세 미만 또는 60개 이상인 승객의 age, sex, alone")
mask3 = (titanic.age < 10) | (titanic.age >= 60)
df_under10_morthan60 = titanic.loc[mask3,['age','sex','alone']]
print(df_under10_morthan60.head(),'\n')

desired_width = 600
pd.set_option('display.width',desired_width)
np.set_printoptions(linewidth = desired_width)
pd.set_option('display.max_columns',15)

print("# 동승자가 3,4,5인 승객만 -불린 인덱싱")
mask3 = titanic['sibsp'] == 3
mask4 = titanic['sibsp'] == 4
mask5 = titanic['sibsp'] == 5
df_boolean = titanic[mask3|mask4|mask5]
print(df_boolean.head())
print()

print("# isin() 메서드 활용하여 동일한 조건으로 추철")
isin_filter = titanic['sibsp'].isin([3,4,5])
df_isin = titanic[isin_filter]
print(df_isin.head())