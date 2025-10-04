# big_data_set1_eda를 DataFrame으로 생성 (예시 데이터 사용)
import pandas as pd

# 예시 데이터 (실제 데이터로 대체하세요)
data = "C:\\Users\\samsung\\OneDrive\\빅콘테스트 AI데이터 경진대회\\0. 제공 데이터\\big_data_set1_f.csv"
big_data_set1_eda = pd.DataFrame(data)

# EDA 진행
print("기본 정보:")
print(big_data_set1_eda.info())
print("\n기술 통계:")
print(big_data_set1_eda.describe(include='all'))
print("\n결측치 확인:")
print(big_data_set1_eda.isnull().sum())
print("\n범주형 변수 분포:")
print(big_data_set1_eda['gender'].value_counts())
print("\n상관관계:")
print(big_data_set1_eda.corr(numeric_only=True))
