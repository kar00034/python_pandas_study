import matplotlib
import pandas as pd
import matplotlib.pyplot as plt


matplotlib.rcParams['font.family'] = 'NanumGothic'
matplotlib.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('./시도별 전출입 인구수.xlsx',fillna=0, header=0)
df = df.fillna(method='ffill')

mask = (df['전출지별']=='서울특별시') & (df['전입지별']!='서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'],axis=1)
df_seoul.rename({'전입지별':'전입지'},axis=1, inplace=True)
df_seoul.set_index('전입지',inplace=True)

col_years = list(map(str, range(2010,2018)))
df_4 = df_seoul.loc[['충청남도','경상북도','강원도','전라남도'],col_years]
df_4 = df_4.transpose()

print(df_seoul.head(),'\n',df_4.head(),'\n')

plt.style.use('ggplot')

df_4.index = df_4.index.map(int)
df_4.plot(kind='bar',figsize=(30,10),width=0.7,color=['orange','green','skyblue','blue'])

plt.title('서울 -> 타시도 인구 이동',size=30)
plt.ylabel('이동 인구 수',size=20)
plt.xlabel('기간',size=20)
plt.ylim(5000,30000)
plt.legend(loc='best',fontsize=15)

plt.show()