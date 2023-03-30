import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from mpl_toolkits.mplot3d import Axes3D

data = pd.read_csv("data/input.csv", header=0)

# 1列目はeNPSとして扱う
enps = data["enps"]

# 2列目以降はスコアデータ
scores = data.drop("enps", axis=1)

# スコア平均を算出
avg_scores = scores.mean()

# eNPSとスコアの相関を算出
cor_enps = scores.apply(lambda x: enps.corr(x), axis=0)

# 二次元散布図を作成
plt.scatter(avg_scores, cor_enps)
plt.axhline(y=cor_enps.mean(), color="#dcdcdc")
plt.axvline(x=avg_scores.mean(), color="#dcdcdc")
plt.show()

# 相関係数の優位性を検定
cor_tests = []
for col in scores:
    cor_test = stats.pearsonr(enps, scores[col])
    cor_tests.append(cor_test[1])

# 3D散布図を作成する
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
colors = np.where(np.array(cor_tests) <= 0.05, "#d52b2b", "#ffd5d5")
ax.scatter(avg_scores, cor_tests, cor_enps, c=colors, marker='o')
ax.set_xlabel('Avg Scores')
ax.set_ylabel('Cor Tests')
ax.set_zlabel('Cor ENPS')

for i, txt in enumerate(scores.columns):
    ax.text(avg_scores[i], cor_tests[i], cor_enps[i], txt)

plt.show()
