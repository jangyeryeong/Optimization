# 바이크 특징 : 시간의 흐름에 따라 데이터가 정리되어 있음, 년 - 월 - 일 - 시간
# 컴퓨터가 문자열로 읽으면 안되므로 계산이 불가능함, 데이터를 쓸 것인가 말 것인가 고민해보기
# 공유 자전거의 사용량

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import seaborn as sns

# season : 1 봄, 2 여름, 3 가을, 4 겨울
# 날씨 : 1 맑음, 2 구름, 3 눈, 4 안개 우박
# 캐쥬얼 : 비회원 이용, 레지스털드 : 회원 이용

df = pd.read_csv('sharing_bike_train.csv')
df["year"] = pd.to_datetime(df["datetime"]).dt.year
df["month"] = pd.to_datetime(df["datetime"]).dt.month
df["day"] = pd.to_datetime(df["datetime"]).dt.day
df["hour"] = pd.to_datetime(df["datetime"]).dt.hour

# 사용자가 많은 날짜 예측...일까...
# 필요한 수준까지 시간을 분리하기 or timestamp 로 변경 ( 레이블 인코딩과 큰 차이 X )



