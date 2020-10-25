import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
import seaborn as sns

# 차트로 뿌려 볼 것
# 이를 가지고 최적의 클러스터 개수가 몇개인지 파악하기
df = pd.read_csv('cluster_sample_1.csv')

distoritions = []

for cluster in range(1, 21):
    km = KMeans(n_clusters=cluster).fit(df[['x', 'y']])
    distance = cdist(df[['x', 'y']], km.cluster_centers_, 'euclidean')

    min_distance = np.min(distance, axis = 1)
    sum_distance = sum(min_distance)

    distoritions.append(sum_distance / df[['x', 'y']].shape[0])

#클러스터가 15개 일 때 가장 최적이다
#plt.plot(range(1, 21), distoritions)
#plt.show()


#plt.scatter(df[['x']], df[['y']])
#plt.show()

km = KMeans(n_clusters=15).fit(df[['x', 'y']])
df['cluster_id'] = km.labels_
sns.lmplot('x', 'y', data = df, hue = 'cluster_id', fit_reg = False)
plt.show()