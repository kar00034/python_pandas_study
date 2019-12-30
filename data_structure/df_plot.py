import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

#한글설정
matplotlib.rcParams['font.family'] = 'NanumGothic'
matplotlib.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('./남북한발전전력량.xlsx')

df_ns = df.iloc[[0,5],3:]
df_ns.index = ['South','North']
df_ns.columns = df_ns.columns.map(int)
print(df_ns.head)
print()

#선그래프 그리기
df_ns.plot(title = '선그래프 그리기')

# 행, 열 전치하여 다시 그리기
tdf_ns = df_ns.T
print(tdf_ns.head())

#plt.subplot(132)
tdf_ns.plot(title = '전치하여 다시 그리기')

plt.show()