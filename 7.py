import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import seaborn as sns

df = pd.read_csv('generator.csv')
sns.lmplot('RPM', 'VIBRATION', data=df, hue='STATUS', fit_reg=False)
plt.show()

train = df.sample(frac=0.9, random_state=200)
test = df.drop(train.index)

logistic = LogisticRegression()
logistic.fit(train[['RPM', 'VIBRATION']], train['STATUS'])
score = logistic.score(test[['RPM', 'VIBRATION']], test['STATUS'])

print(score)
