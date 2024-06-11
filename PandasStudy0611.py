import pandas as pd

# 데이터 생성
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

# DataFrame 생성
df = pd.DataFrame(data)

# DataFrame 출력
print(df)

# 상위 5개의 데이터 조회 (기본값은 5)
print(df.head())

# 하위 5개의 데이터 조회
print(df.tail())

# DataFrame의 요약 정보 확인
print(df.info())

# 데이터 통계 요약 확인
print(df.describe())

# 'Name' 열만 선택
print(df['Name'])

# 여러 열 선택
print(df[['Name', 'City']])