# 목표 데이터가 주여졌을 때 이탈할 수 있는 고객인지 확인하기

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import seaborn as sns

df = pd.read_csv('telecom_churn.csv')  # 학습용 데이터
df.dropna(inplace=True)  # 값이 없는 것은 삭제해주는 코드

le = LabelEncoder()
df['gender'] = le.fit_transform(df['gender'])
df['SeniorCitizen'] = le.fit_transform(df['SeniorCitizen'])
df['Partner'] = le.fit_transform(df['Partner'])
df['Dependents'] = le.fit_transform(df['Dependents'])
df['PhoneService'] = le.fit_transform(df['PhoneService'])
df['MultipleLines'] = le.fit_transform(df['MultipleLines'])
df['InternetService'] = le.fit_transform(df['InternetService'])
df['OnlineSecurity'] = le.fit_transform(df['OnlineSecurity'])
df['OnlineBackup'] = le.fit_transform(df['OnlineBackup'])
df['DeviceProtection'] = le.fit_transform(df['DeviceProtection'])
df['TechSupport'] = le.fit_transform(df['TechSupport'])
df['StreamingTV'] = le.fit_transform(df['StreamingTV'])
df['StreamingMovies'] = le.fit_transform(df['StreamingMovies'])
df['Contract'] = le.fit_transform(df['Contract'])
df['PaperlessBilling'] = le.fit_transform(df['PaperlessBilling'])
df['PaymentMethod'] = le.fit_transform(df['PaymentMethod'])
df['Churn'] = le.fit_transform(df['Churn'])

logistic = LogisticRegression(solver='newton-cg')
logistic.fit(df[["gender", "SeniorCitizen", "Partner", "Dependents", "tenure", "PhoneService",
                 "MultipleLines", "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection",
                 "TechSupport", "StreamingTV", "StreamingMovies", "Contract", "PaperlessBilling",
                 "PaymentMethod", "MonthlyCharges", "TotalCharges"]], df["Churn"])

# sns.lmplot('tenure', 'OnlineBackup', data=df, hue='Churn', fit_reg=False)
# plt.show()

# train = df.sample(frac=0.8, random_state=200)
# test = df.drop(df.index)

# logistic = LogisticRegression()
# logistic.fit(df[['tenure', 'OnlineBackup']], df['Churn'])
# score = logistic.score(test[['tenure', 'OnlineBackup']], test['Churn'])

# print(score)

# 카테고리에 해당하는 데이터가 문자로 되있으면 분류가 안된다! 회귀 분석을 하려면 데이터는 숫자로 치환해야한다 => 카테고리 수식화

# one hot encoding : 하나의 값만 True 나머지는 모두 False
# 오차가 섞일 확률이 적다
# label encoding : 문자로 표현된 레이블을 숫자 형태로 바꾸는 과정, 카테고리가 있을 때 첫번째껀 1, 두번째껀 2.. 이런 식으로 나눔
# 카테고리 갯수 숫자를  늘린다.., 오차가 생길 확률이 적다

# 하지만 에러가 발생한다면 ...!!
# 영향을 주지않을 값을 주거나 값이 없는 항목을 제거하는 것이 필요함
# ex ) 통신비에서 값이 안나와있는 부분을 제거 !

dd = pd.read_csv('telecom_churn_test.csv')
dd.dropna(inplace=True)

dd['gender'] = le.fit_transform(dd['gender'])
dd['SeniorCitizen'] = le.fit_transform(dd['SeniorCitizen'])
dd['Partner'] = le.fit_transform(dd['Partner'])
dd['Dependents'] = le.fit_transform(dd['Dependents'])
dd['PhoneService'] = le.fit_transform(dd['PhoneService'])
dd['MultipleLines'] = le.fit_transform(dd['MultipleLines'])
dd['InternetService'] = le.fit_transform(dd['InternetService'])
dd['OnlineSecurity'] = le.fit_transform(dd['OnlineSecurity'])
dd['OnlineBackup'] = le.fit_transform(dd['OnlineBackup'])
dd['DeviceProtection'] = le.fit_transform(dd['DeviceProtection'])
dd['TechSupport'] = le.fit_transform(dd['TechSupport'])
dd['StreamingTV'] = le.fit_transform(dd['StreamingTV'])
dd['StreamingMovies'] = le.fit_transform(dd['StreamingMovies'])
dd['Contract'] = le.fit_transform(dd['Contract'])
dd['PaperlessBilling'] = le.fit_transform(dd['PaperlessBilling'])
dd['PaymentMethod'] = le.fit_transform(dd['PaymentMethod'])
dd['Churn'] = le.fit_transform(dd['Churn'])


score = logistic.score(dd[["gender", "SeniorCitizen", "Partner", "Dependents", "tenure", "PhoneService",
                           "MultipleLines", "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection",
                           "TechSupport", "StreamingTV", "StreamingMovies", "Contract", "PaperlessBilling",
                           "PaymentMethod", "MonthlyCharges", "TotalCharges"]], dd["Churn"])
print(score)
