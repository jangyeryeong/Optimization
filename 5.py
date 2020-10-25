#위도나 경도를 가지고 동을 예측
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns

df = pd.read_csv('seoul.csv')
label_count = len(df['name'].unique()) #데이터가 몇개인지 카운트 해줌
sns.lmplot('lat', 'lon', data = df, hue = 'name', fit_reg = False) #기억안남..
plt.show()

train = df.sample(frac = 0.8, random_state = 200)
test = df.drop(train.index)

knn = KNeighborsClassifier(n_neighbors = label_count)
knn.fit(train[['lat', 'lon']], train['name'])
score = knn.score(test[['lat', 'lon']], test['name'])
print(score)

guess = pd.DataFrame(columns = ['lat', 'lon'])
guess.loc[0] = [37.532015, 127.120230]
print(knn.predict(guess)) #데이터 점수가 바뀜, 데이터의 평균적인 위치가 바뀜... 한계가 있다...

# KNN 카테고리가 정해져있는 경우 리니어 어떠한 값이 더 나음에 따라 바뀔꺼다!!