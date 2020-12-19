# options(rgl.useNULL=TRUE)
# .rs.restartR()
library("rgl")

data <- read.csv("data/input.csv", header=TRUE)

# 1列目はeNPSとして扱う
enps <- data[,1]

# 2列目以降はスコアデータ
scores <- data[2:length(data)]

# スコア平均を算出
avg_scores <- apply(scores, 2, mean)

# eNPSとスコアの相関を算出
cor_enps <- cor(enps, scores)

# 二次元散布図を作成
plot(avg_scores, cor_enps, type = "n")
abline(h = mean(cor_enps), v = mean(avg_scores), col="#dcdcdc")
text(avg_scores, cor_enps)

# 相関係数の優位性を検定
cor_tests <- vector(mode = "numeric",)
for (score in scores) {
  cor_test <- cor.test(enps, score)
  cor_tests <- c(cor_tests, cor_test$p.value)
}

# 3D散布図を作成する
plot3d(avg_scores, cor_tests, cor_enps, type = "h", col = ifelse(cor_tests <= 0.05, "#d52b2b", "#ffd5d5"))
text3d(avg_scores, cor_tests, cor_enps, c(1:length(cor_enps)))
grid3d("x", at = list(x = mean(avg_scores)), col = "#dcdcdc") 
grid3d("z", at = list(z = mean(cor_enps)), col = "#dcdcdc")