# https://www.yorku.ca/mack/RN-HowToReportAnFStatistic.html
natural <- c(656,259,612,609,1049,1135,542,495,905,715)
abstract <- c(702,339,658,645,1129,1179,604,551,893,803)
df <- data.frame(natural, abstract)
str(df)
summary(df)

#reshape
#install.packages("tidyverse")
library(tidyverse)
df <- df %>%
  rownames_to_column(var = "Name") %>%      # tibble
  gather(Icon, Value, -Name)
#df <- df %>% gather(Icon, Value)
df$Icon <- as.factor(df$Icon)
str(df)

aggregate(Value ~ Icon,
          data = df,
          function(x) round(c(mean = mean(x), sd = sd(x)), 2)
)
par(mfrow = c(1, 1))
boxplot(df$Value ~ df$Icon)

#anova
summary(aov(df$Value ~ df$Icon))

summary(aov(df$Value ~ df$Icon + df$Name)) # actually non-sense to stratify for individuals?!

summary(aov(df$Value ~ df$Icon + df$Name + df$Icon:df$Name))
summary(aov(df$Value ~ df$Icon * df$Name)) # same

# iris
# https://www.beratung-statistik.de/statistik-beratung-infos/r-tutorial/r-varianzanalyse-post-hoc/
head(iris,10)
str(iris)
boxplot(iris$Sepal.Length ~ iris$Species)
summary(aov(iris$Sepal.Length ~ iris$Species))
TukeyHSD(aov(iris$Sepal.Length ~ iris$Species)) 

# penguins
# https://statsandr.com/blog/anova-in-r/
# install.packages("palmerpenguins")
library(palmerpenguins)
library(tidyverse)
dat <- penguins %>%
  select(species, flipper_length_mm)
summary(dat)
# plot
library(ggplot2)
ggplot(dat) +
  aes(x = species, y = flipper_length_mm, color = species) +
  geom_jitter() +
  theme(legend.position = "none")
#anova
res_aov <- aov(flipper_length_mm ~ species,
               data = dat
)
#check normality
par(mfrow = c(1, 2)) # combine plots

# histogram
hist(res_aov$residuals)

# QQ-plot
# see https://github.com/lme4/lme4/issues/656
# devtools::install_github('cran/nloptr@1.2.2.3')
# install.packages('lme4')
# install.packages("car")
library(car)
qqPlot(res_aov$residuals,
       id = FALSE # id = FALSE to remove point identification
)
shapiro.test(res_aov$residuals)

aggregate(flipper_length_mm ~ species,
          data = dat,
          function(x) round(c(mean = mean(x), sd = sd(x)), 2)
)

res_aov <- aov(flipper_length_mm ~ species,
               data = dat
)

summary(res_aov)
