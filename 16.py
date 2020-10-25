# 선형회귀를 평가하는 방법
# 1. R2 score : 얼마만큼 영향을 가지고 있는가 지표 결정계수 : 성능 ( 얼마만큼 잘 맞추는지 ) 얼마나 좋은지 상대적으로 알려줌 확률, 2. 차트로 예상 값 비교

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn import metrics

df = pd.read_csv('sharing_bike_train.csv')

df['year'] = pd.to_datetime(df['datetime']).dt.year
df['month'] = pd.to_datetime(df['datetime']).dt.month
df['day'] = pd.to_datetime(df['datetime']).dt.day
df['hour'] = pd.to_datetime(df['datetime']).dt.hour
df['weekday'] = pd.to_datetime(df['datetime']).dt.weekday

del df['datetime']
del df['casual']
del df['registered']
# 카운트를 구해야해서 삭제안함

df['year'] = df['year'].astype('category')
df['month'] = df['month'].astype('category')
df['day'] = df['day'].astype('category')
df['hour'] = df['hour'].astype('category')
df['weekday'] = df['weekday'].astype('category')
df['season'] = df['season'].astype('category')
df['weather'] = df['weather'].astype('category')

df = pd.get_dummies(df)

print(df.columns.tolist())