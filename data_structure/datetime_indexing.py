import pandas as pd

from data_structure.set_dis import set_dis

df = pd.read_csv('stock-data.csv')
set_dis(len(df.columns), int(df['Date'].apply(len).max()), 600)

print("# 문자열인 날짜 데이터를 판다스 Timestamp로 변환")
df['new_Date'] = pd.to_datetime(df['Date'])
df.set_index('new_Date',inplace=True)

print(df.head(),'\n',df.index,'\n')

print("#날짜 인덱스를 이용하여 데이터 선택하기")
df_y = df['2018']
print(df_y.head(),'\n')

print("# loc 인덱서 활용")
df_ym = df.loc['2018-07']
print(df_ym,'\n')

print("# 열 범위 슬라이싱")
df_ym_cols = df.loc['2018-07','Start':'High']
print(df_ym_cols,'\n')
df_ymd = df['2018-07-02']
print(df_ymd,'\n')

print("# 날짜 범위 지정")
df_ymd_range = df['2018-06-25':'2018-06-20']
print(df_ymd_range,'\n')

print("# 시간 간격 계산. 최근 180일 ~ 189일 사이의 값들만 선택하기")
today = pd.to_datetime('2018-12-25')
df['time_delta'] = today - df.index
df.set_index('time_delta', inplace=True)
df_180 = df['180 days':'189 days']
print(df_180)