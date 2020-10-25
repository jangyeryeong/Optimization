import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('sharing_bike_train.csv')
df["year"] = pd.to_datetime(df["datetime"]).dt.year
df["month"] = pd.to_datetime(df["datetime"]).dt.month
df["day"] = pd.to_datetime(df["datetime"]).dt.day
df["hour"] = pd.to_datetime(df["datetime"]).dt.hour

del df["datatime"]
del df["regist"]
del df["datatime"]

# one hot encoding 을 하게되면 모든 속성의 이름을 나열하는게 쉽지 않음, 데이터 분리를 통 데이터 사용
# 모르는 데이터를 분석하는 법 : 1. 목표값 설정, 카테고리성 데이터가 2개 이면 로지스틱 2개 이상이면 KNN
# 속성에 의해 변화되는 수치가 있는 경우 : Linear Regression 사용

df = pd.get_dummies(df) # 자동으로 바꿔줌

del df["datatime"]
