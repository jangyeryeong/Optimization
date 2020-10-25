import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist

data = [[7, 1], [2, 1], [4, 2], [9, 4], [10, 5], [10, 6], [11, 5], [11, 6], [11, 6], [15, 3], [15, 2], [16, 4], [16, 1]]

df = pd.DataFrame(columns=['x', 'y'], data = data)

distoritions = []

for cluster in range(1, 10):
    km = KMeans(n_clusters=cluster).fit(df[['x', 'y']])
    # 중심점과 모든 좌표들간의 거리 (N : N)
    # 평균적으로 가장 중간에 있는 것을 중심점으로 만듬, 중심점이란 모든 데이터들 간의 거리를 뉴클리디안 디스턴스로 표현함
    # 클러스터의 중심점과 데이터의 좌표를 나타냄
    distance = cdist(df[['x', 'y']], km.cluster_centers_, 'euclidean')

    # 중심점 좌표간 거리 중 최저인 값
    # min_distance 각 점 별로 중심점과 거리가 제일 가까운 점
    # sum_distance 거리가 제일 짧은 점들의 합
    min_distance = np.min(distance, axis = 1)
    sum_distance = sum(min_distance)

    # 평균 최소거리의 합
    # len() 으로 바꿔도 됨
    distoritions.append(sum_distance / df[['x', 'y']].shape[0])

# 급격하게 바뀌는 부분이 최적일 가능성이 높다
# 적당하게 쪼개는게 중요하다 훨신 더 범용성 있는 데이터를 만들 수 있는 확률이 증가하기 때문이다
plt.plot(range(1, 10), distoritions)
plt.show()