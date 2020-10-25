from sklearn.datasets import load_boston #1960년 보스턴 집 값에 관한 데이터
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import pandas as pd

boston_data = load_boston() #보스턴 집 값 정보를 불러오는 함수

boston = pd.DataFrame(data=boston_data.data, columns=boston_data.feature_names) #데이터 프레임 기준으로 데이터를 만들고 처리함, 이차원 배열, 항의 이름에 관련됨
boston['target'] = boston_data.target #y의 값에 해당 (집값)

train = boston.sample(frac=0.8, random_state = 200) #데이터의 80%를 샘플링, 샘플링 : 샘플로 추출하는 행위
test = boston.drop(train.index)

scatter_matrix(boston.drop(columns=["B","CRIM","ZN","INDUS","CHAS","NOX","AGE","DIS","RAD","TAX","PTRATIO","LSTAT"]))
plt.show()

