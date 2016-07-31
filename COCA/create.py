# import data
import pandas as pd
df = pd.read_csv('MetaData/top5000_add_all_label.csv')

# select data
df_1000_2000 = df[1000：2000]
df_1000_2000 = df_1000_2000[df_1000_2000.Know==1]
df_2_1_100 = df_1000_2000[:100]

# produce data
df_2_1_100_values = df_2_1_100['Word']
df_2_1_100_rename = df_2_1_100[['Rank', 'Word']]
df_2_1_100_all = df_2_1_100[['Rank','Word','Part of speech']]

# export data
df_2_1_100_all.to_csv('Rename&Values/df_2_1_100_all.txt', index=False, header=False)
df_2_1_100_values.to_csv('SplitData/df_2_1_100_values.txt', index=False, header=False)
df_2_1_100_values.to_csv('Rename&Values/df_2_1_100_values.txt', index=False, header=False)
df_2_1_100_rename.to_csv('Rename&Values/df_2_1_100_rename.txt', index=False, header=False)
