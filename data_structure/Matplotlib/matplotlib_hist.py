import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('classic')

df = pd.read_csv('../auto-mpg.csv', header=None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']

df['mpg'].plot(kind='hist',bins=10,color='coral',figsize=(10,5))

plt.title('Histogram')
plt.xlabel('mpg')
print(df['mpg'].value_counts())
plt.show()