# 시간별 자전거 수 예측!! 18 => 오후 6시
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn.linear_model import LinearRegression
import seaborn as sns

bk = pd.read_csv('sharing_bike_train.csv')

train = bk.sample(frac=0.8, random_state=200)
test = bk.drop(train.index)

scatter_matrix(columns=["datetime","season","holiday","workingday","weather","temp","atemp","humidity","windspeed","casual","registered","count"])
plt.show()

# mlr = LinearRegression()
# mlr.fit(train[['PTRATIO','INDUS','NOX','B','CHAS','RAD','TAX','ZN','DIS','CRIM','RM','LSTAT','AGE']], train['target'])
# #함수x값, y값 이렇게친거임
# print(mlr.intercept_) #절편
# print(mlr.coef_) #기울기
#
# sum_difference = 0
# for i, row in test.iterrows():
#     estimate = row['PTRATIO'] * mlr.coef_[0] + row['INDUS'] * mlr.coef_[1] + row['NOX']* mlr.coef_[2] + \
#         row['B']* mlr.coef_[3] + row['CHAS'] * mlr.coef_[4] + row['RAD'] * mlr.coef_[5] + \
#         row['TAX'] * mlr.coef_[6] + row['ZN'] * mlr.coef_[7] + row['DIS'] * mlr.coef_[8] + \
#         row['CRIM'] * mlr.coef_[9] + row['RM'] * mlr.coef_[10] + row['LSTAT'] * mlr.coef_[11] + \
#         row['AGE'] * mlr.coef_[12] + mlr.intercept_
#
#     difference = abs(row['target'] - estimate) #오차 = 실제 - 예측
#     sum_difference += difference
#
# print(sum_difference)