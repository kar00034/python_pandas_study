import pandas as pd

def set_dis(col=5,colwidth=20,width=400):
    pd.set_option('display.max_columns',col)                  #출력할 최대 열의 개수
    pd.set_option('display.max_colwidth', colwidth)           #출력할 열의 너비
    pd.set_option('display.unicode.east_asian_width',True)    #유니코드 사용 너비 조정
    pd.set_option('display.width', width)                     #출력할 출력 너비
    #len(df.columns), int(df['Date'].apply(len).max()), 600