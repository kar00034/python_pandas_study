import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

from pandas_study.data_structure.set_dis import set_dis

df = pd.read_excel('./시도별 전출입 인구수.xlsx',fillna=0, header=0)

matplotlib.rcParams['font.family'] = 'NanumGothic'
matplotlib.rcParams['axes.unicode_minus'] = False

set_dis(10,20,600)
df = df.fillna(method='ffill')

#서울에서 다른 지역으로 이동한 데이터만 추출하여 정리
mask = (df['전출지별']=='서울특별시') & (df['전입지별']!='서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'],axis=1)
df_seoul.rename({'전입지별':'전입지'},axis=1, inplace=True)
df_seoul.set_index('전입지',inplace=True)

# 서울에서 경기도로 이동한 인구 데이터 값만 선택
sr_one = df_seoul.loc['경기도']

# 스타일 서식 지정
plt.style.use('ggplot')

fig = plt.figure(figsize=(20,5))
fig.subplots_adjust(left=0.2,right=0.8,bottom=0.2,top=0.87,wspace=0.3,hspace=0.5)
ax = fig.add_subplot(1,1,1)

ax.plot(sr_one,marker='o',markerfacecolor='orange',markersize=5,color='olive',linewidth=2,label='서울->경기')
ax.legend(loc='best')

#y축 범위 지정(최소,최대)
ax.set_ylim(50000,800000)

#차트 제목
ax.set_title('서울 -> 경기 인구 이동')

#축 이름 추가
ax.set_xlabel('기간')
ax.set_ylabel('이동인구수')

#축 눈금 라벨 지정 및 75도 회전
ax.set_xticklabels(sr_one.index,rotation=75)

#축 눈금 라벨 크기
ax.tick_params(axis="x",labelsize=10)
ax.tick_params(axis="y",labelsize=10)

plt.show()