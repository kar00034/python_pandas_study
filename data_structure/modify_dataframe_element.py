import pandas as pd

exam_data = {'이름':['서준','우현','인아'],'수학':[90,80,70],'영어':[98,89,95],'음악':[85,95,100],'체육':[100,90,90]}
df = pd.DataFrame(exam_data)
print(df)
print()

print("# '이름'열을 새로운 인덱스로 지정하고, df 객체에 변경사항 반영")
df.set_index('이름',inplace=True)
print(df)
print()

print("# 데이트프레임 df의 특정 원소를 연결하는 방법: '서준'의 '체육'점수")
df.iloc[0][3]=80
print(df)
print()

df.loc['서준']['체육']=90
print(df)
print()

df.loc['서준']['체육']=100
print(df)
print()

print("# 데이터프레임 df의 원소 여러 개를 변경하는 방법:'서준'의'음악','체육' 점수")
df.loc['서준',['음악','체육']]=50
print(df)
print()

df.loc['서준',['음악','체육']]=100,50
print(df)