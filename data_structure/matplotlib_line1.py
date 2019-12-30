import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager, rc

from data_structure.set_dis import set_dis

df = pd.read_excel('./시도별 전출입 인구수.xlsx',fillna=0, header=0)

matplotlib.rcParams['font.family'] = 'NanumGothic'
matplotlib.rcParams['axes.unicode_minus'] = False

set_dis(10,20,600)

print(df.head())

df = df.fillna(method='ffill')
print(df.head())

#서울에서 다른 지역으로 이동한 데이터만 추출하여 정리
mask = (df['전출지별']=='서울특별시') & (df['전입지별']!='서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'],axis=1)
df_seoul.rename({'전입지별':'전입지'},axis=1, inplace=True)
df_seoul.set_index('전입지',inplace=True)

print(df_seoul.head())

# 서울에서 경기도로 이동한 인구 데이터 값만 선택
sr_one = df_seoul.loc['경기도']
print(sr_one.head())

# plt.plot(sr_one.index,sr_one.values)
plt.xticks(rotation=45)

# plt.plot(sr_one)

plt.plot(sr_one)
plt.title('서울-> 경기 인구 이동')

plt.xlabel('기간')
plt.ylabel('이동 인구수')

plt.legend(['서울 -> 경기'],loc='best')
plt.show()

