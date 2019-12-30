import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv('./auto-mpg.csv',header=None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']

#한글설정
matplotlib.rcParams['font.family'] = 'NanumGothic'
matplotlib.rcParams['axes.unicode_minus'] = False

df[['mpg','cylinders']].plot(kind='box',title='연비의 분포 및 실린더개수 분포')

plt.show()