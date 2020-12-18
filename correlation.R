# options(rgl.useNULL=TRUE)
# .rs.restartR()
library("rgl")

data <- read.csv("data/input.csv", header=TRUE)

# 1行目はeNPSとして扱う
enps <- data[,1]

# 2行目以降はスコアデータ
scores <- data[2:length(data)]

# スコア平均を算出
avg_score <- apply(scores, 2, mean)

# eNPSとスコアの相関を算出
cor_enps <- cor(enps, scores)

# 二次元散布図を作成
#plot(avg_score, cor_enps, type = "n")
#text(avg_score, cor_enps)

# 相関係数の優位性を検定
cor_tests <- vector(mode = "numeric",)
for (score in scores) {
  cor_test <- cor.test(enps, score)
  cor_tests <- c(cor_tests, cor_test$p.value)
}

plot3d(avg_score, cor_tests, cor_enps, type = "n")
text3d(avg_score, cor_tests, cor_enps, c(1:length(cor_enps)))