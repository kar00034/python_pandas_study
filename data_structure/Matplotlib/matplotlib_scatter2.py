import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')

df=pd.read_csv('../auto-mpg.csv')
df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']

cylinder_size=df.cylinders/df.cylinders.max()*300

df.plot(kind='scatter',x='weight',y='mpg',c='coral',figsize=(10,5),s=cylinder_size,alpha=0.3)
plt.title('Scatter Plot: mpg-weight-cylinders')
plt.show()