import pandas as pd

# DataFrame() 함수로 데이터 프레임 변환, 변수 df에 저장
exam_data = {'이름':['서준','우현','인아'],'수학':[90,80,70],'영어':[98,89,95],'음악':[85,95,100],'체육':[100,90,90]}
df = pd.DataFrame(exam_data)

print("# '이름'열을 새로운 인덱스로 지정하고, df객체에 변경사항 반영")
df.set_index('이름',inplace=True)
print(df)
print()

print("# 데이터프레임 df의 특정원소 1개 선택('서준'의 '음악' 점수)")
a = df.loc['서준','음악']
print(a,type(a),sep=' ')
b = df.iloc[0,2]
print(b,type(b),sep=' ')
print()

print("# 데이터프레임 df의 특정원소 2개 이상 선택('서준', '우현'의 '음악','체육' 점수")
g = df.loc[['서준','우현'],['음악','체육']]
print(g,type(g),sep='\n')
h = df.iloc[[0,1],[2,3]]
print(h,type(h),sep='\n')
i = df.loc['서준':'우현','음악':'체육']
print(i,type(i),sep='\n')
j = df.iloc[0:2, 2:]
print(j,type(j),sep='\n')