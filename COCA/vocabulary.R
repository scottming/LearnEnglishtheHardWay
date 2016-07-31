library(readr)
library(dplyr)
library(utils)
df <- read_csv(file = '~/Documents/LearnEnglish/MetaData/top5000_add_all_label.csv')
df

df1 <- filter(df, Know == 1, Rank < 2000) %>%
  filter(Rank > 1000)
df2 <- select(df1, Word)

write_csv(df1, '~/vocabulary_1000_2000.csv')
write_csv(df2, '~/vocabulary_1000_2000_value.csv', col_names = FALSE)

df3 <- df2[0:100, ]
?slice
summary(slice(df, 10L))



