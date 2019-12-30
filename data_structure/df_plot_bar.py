import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_excel('./남북한발전전력량.xlsx')

df_ns = df.iloc[[0,5],3:]
df_ns.index = ['남한','북한']
df_ns.columns = df_ns.columns.map(int)

# 행, 열 전치하여 막대그래프 그리기
tdf_ns = df_ns.T
print(tdf_ns.head())
print('\n')

#한글설정
matplotlib.rcParams['font.family'] = 'NanumGothic'
matplotlib.rcParams['axes.unicode_minus'] = False

tdf_ns.plot(kind='bar',title='남북한 발전 전력량')

plt.show()