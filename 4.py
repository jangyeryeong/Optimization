import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns

df = pd.read_csv('generator.csv')
sns.lmplot('RPM', 'VIBRATION', data = df, hue = 'STATUS', fit_reg = False)
plt.show()

train = df.sample(frac = 0.8, random_state = 200)
test = df.drop(train.index)

knn = KNeighborsClassifier(n_neighbors = 2) # 레이블 두 개를 넣어줌
knn.fit(train[['RPM', 'VIBRATION']], train['STATUS']) # RPM, VIBRATION 을 기준으로 STATUS 가 나옴!, fit 학습을 시키라는 의미
score = knn.score(test[['RPM', 'VIBRATION']], test['STATUS']) #score 점수를 매김, 내가 test 한거랑 train 을 비교

print(score) # 1 이 100퍼센트를 의미 함

#knn의 방식, 점을 찍었을 때 인접한 점을 확인하고 faulty인지 good 인지 확인함
guess = pd.DataFrame(columns=['RPM', 'VIBRATION'])
guess.loc[0] = [750, 200]
print(knn.predict(guess))
