import matplotlib
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('Seaborn-poster')
matplotlib.rcParams['font.family'] = 'NanumGothic'
matplotlib.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('auto-mpg.csv',header=None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']

fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
ax3 = fig.add_subplot(2,2,1)

ax1.boxplot(x=[df[df['origin']==1]['mpg'],df[df['origin']==2]['mpg'],df[df['origin']==3]['mpg']],labels=['USA','EU','JAPAN'])
ax2.boxplot(x=[df[df['origin']==1]['mpg'],df[df['origin']==2]['mpg'],df[df['origin']==3]['mpg']],labels=['USA','EU','JAPAN'],vert=False)
ax3.bar

ax1.set_title('제조국가별 연비 분포(수직 박스 플롯)')
ax2.set_title('제조국가별 연비 분포(수평 박스 플롯)')

plt.show()
