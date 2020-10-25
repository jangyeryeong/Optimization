# 6시의 자전거 수 예측
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('sharing_bike_train.csv')
df["year"] = pd.to_datetime(df["datetime"]).dt.year
df["month"] = pd.to_datetime(df["datetime"]).dt.month
df["day"] = pd.to_datetime(df["datetime"]).dt.day
df["hour"] = pd.to_datetime(df["datetime"]).dt.hour

train = df.sample(frac=0.8, random_state=200)
test = df.drop(train.index)

mlr = LinearRegression()
mlr.fit(train[["season","holiday","workingday","weather","temp","atemp","humidity","windspeed"]], train['count'])  # 순서대로 나옴, 캐쥬얼이랑 레지스터드를 합치면 카운트
print(mlr.intercept_)  # 절편
print(mlr.coef_) # 계수

sum_difference = 0
#기울기, 독립변인을 찾기 위해
for i, row in test.iterrows():
    estimate = row['season'] * mlr.coef_[0] + row['holiday'] * mlr.coef_[1] + row['workingday'] * mlr.coef_[2] + \
               row['weather'] * mlr.coef_[3] + row['temp'] * mlr.coef_[4] + row['atemp'] * mlr.coef_[5] + \
               row['humidity'] * mlr.coef_[6] + row['windspeed'] * mlr.coef_[7] + mlr.intercept_

    difference = abs(row['count'] - estimate) # 오차 = 실제 - 예측
    sum_difference += difference # 얼마만큼의 차이가 나는지..
    print(difference)


print(estimate)

print(sum_difference)

# 라벨링 코딩 단점 0으로 시작하면 곱하면 0이 된다... 1은 영향이 있는 애임.. 오차를 줄여줌


