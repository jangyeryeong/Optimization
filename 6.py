#과일의 색깔 크기를..
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns

df = pd.read_csv('fruit_data_with_colors.csv')
label_count = len(df['fruit_label'].unique()) #데이터가 몇개인지 카운트 해줌
sns.lmplot('width', 'color_score', data = df, hue = 'fruit_name', fit_reg = False) #기억안남
plt.show()

train = df.sample(frac = 0.8, random_state = 200)
test = df.drop(train.index)

knn = KNeighborsClassifier(n_neighbors = label_count)
knn.fit(train[['width', 'color_score', 'mass', 'height']], train['fruit_label'])
score = knn.score(test[['width', 'color_score', 'mass', 'height']], test['fruit_label'])
print(score)

# 아웃 라이어, 평균 밖에 있는 이상한 값 때문에 식별이 안 될 수도 있다..! 데이터가 뭉쳐있어 있어도 문제가 생길 수 있다.
# 표준편차, 확률과 통계 => 기준이 확률과 통계로 이루어짐, 정확한 예측이 어렵다!
# 이를 해결하기 위해 임계점을 설정하기도 함.
# 수치를 분석하는 것 => 회귀분석, 수치를 분석했던 값을 기준으로 임계점을 정해서 응용을 할 수도 있다.
