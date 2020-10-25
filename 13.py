import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('sharing_bike_train.csv')

# 사람이 볼 수 있는 시간으로 표현함, 컴퓨터가 보여주는 데이터는 사람이 읽기 쉬운 용도임
df['year'] = pd.to_datetime(df['datetime']).dt.year
df['month'] = pd.to_datetime(df['datetime']).dt.month
df['day'] = pd.to_datetime(df['datetime']).dt.day
df['hour'] = pd.to_datetime(df['datetime']).dt.hour
df['weekday'] = pd.to_datetime(df['datetime']).dt.weekday

# 날씨에 영향을 끼치지 않을 데이터 삭제

del df['datetime']
del df['casual']
del df['registered']
del df['count']

df['year'] = df['year'].astype('category')
df['month'] = df['month'].astype('category')
df['day'] = df['day'].astype('category')
df['hour'] = df['hour'].astype('category')
df['weekday'] = df['weekday'].astype('category')
df['season'] = df['season'].astype('category')
# season 이라고 가정하면 1,2,3,4인데 이걸 내부적으로 분류( 숫자 1, 숫자 2, .. ) 라고 정의를 한 것이다.. 컴퓨터가 알아 처먹기 쉽게 바꿈.. ㅇㅋ? ㅇㅋ ^^7
# 종류만 인식하게 바꿈, 계산에 사용되지 않을 값으로 바꿈

df = pd.get_dummies(df)

# sample : 일부 추출 근데 그 기준을 80% 뽑고 랜덤값을 랜덤을 얼마만큼 줄 것인가...
# 학습용 데이터
train = df.sample(frac=0.8, random_state=200)
# 검증용 데이터, drop : 안에 있는 데이터를 삭제함, 나머지 20%를 가지고 테스트를 함
test = df.drop(train.index) # 없는 번호를 찾음...

# 목표한 데이터 ( 날씨값 )
# x와 y에 해당하는 값을 분류함
train_y = train['weather']
# 사용하지 않을 데이터를 지움, 학습에 필요한 데이터의 속성만 집어넣음
del train['weather']
train_x = train

test_y = test['weather']
del test['weather']
test_x = test

# 모든걸 카테고리 처리함..
print(df.shape)

# 오버피팅, 학습데이터가 딱 맞아떨어지는 것, 다른 데이터가 들어가면 맞추지 못하는 현상을 방지하기 위함
# 언더피팅, 데이터를 너무 못맞춤
# 테스트랑 트레인을 분류하는 이유는 트레인은 내가 생각하는 가설을 검증하는데 사용

# 자기 주변에 있는 데이터를 확인해서 위치를 확인하는 것.. 눈치보기, 바꿔보면서 테스트를 해야하는 값
knn = KNeighborsClassifier(n_neighbors=2)
knn.fit(train_x, train_y)
score = knn.score(test_x, test_y)
print(score)


