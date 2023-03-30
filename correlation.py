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

# 相関係数の優位性を検定
cor_tests = []
for col in scores:
    cor_test = stats.pearsonr(enps, scores[col])
    cor_tests.append(cor_test[1])

colors = np.where(np.array(cor_tests) <= 0.05, "#d52b2b", "#ffd5d5")

# 二次元散布図を作成
plt.scatter(avg_scores, cor_enps, c=colors)

# ラベルをセット
headers = list(scores.columns)
for i, header in enumerate(headers):
    plt.annotate(header, (avg_scores[i], cor_enps[i]))

plt.axhline(y=cor_enps.mean(), color="#dcdcdc")
plt.axvline(x=avg_scores.mean(), color="#dcdcdc")
plt.xlabel("Average Scores")
plt.ylabel("Correlation with eNPS")
plt.title("2D Scatter Plot")
plt.grid(False)
plt.show()

# 3D散布図を作成
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(avg_scores, cor_tests, cor_enps, c=colors, marker='o')
ax.set_xlabel('Avg Scores')
ax.set_ylabel('Cor Tests')
ax.set_zlabel('Cor ENPS')

for i, txt in enumerate(scores.columns):
    ax.text(avg_scores[i], cor_tests[i], cor_enps[i], txt)

plt.show()
