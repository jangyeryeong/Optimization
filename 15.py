import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import logistic
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import seaborn as sns

# 광고를 듣고 그 사람이 적금을 넣었을지 예측

df = pd.read_csv('bank_marketing_simple.csv', sep=';')

df = pd.get_dummies(df, columns=['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'day', 'month',
                                 'poutcome'])

logistic = LogisticRegression(solver='newton-cg')
logistic.fit(df[['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'day', 'month','poutcome']], df["y"])

# s1 = ["age","job","marital","education","default","balance","housing","loan","contact","day","month","duration","campaign","pdays","previous","poutcome"]
# pd.get_dummies(df, columns= ["age","balance","loan","contact","duration","campaign"])

# logistic = LogisticRegression(solver='newton-cg')
# logistic.fit(df[["age","job","marital","education","default","balance","housing","loan","contact","day","month","duration","campaign","pdays","previous","poutcome"]], df["y"])

#train = df.sample(frac=0.8, random_state=200)
#test = df.drop(train.index)

#train_y = train['y']
#del train['y']
#train_x = train

#test_y = test['y']
#del test['y']
#test_x = test

# solver 을 쓰는 것은 알고리즘으로 바꾼다는 뜻, 기본으로 바꾸면 처리할 수 있는 것에 한계가 있으므로 많은 양을 처리하기 위해 뉴턴 cg를 사용한다.
#logistic = LogisticRegression(solver='newton-cg')
#logistic.fit(train_x, train_y)

#score = logistic.score(test_x, test_y)
#print(score)

dd = pd.read_csv('bank_marketing_full.csv', sep=';')
dd = pd.get_dummies(dd, columns=['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'day', 'month',
                                 'poutcome'])

score = logistic.score(dd[['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'day', 'month', 'poutcome']], dd["y"])
print(score)
