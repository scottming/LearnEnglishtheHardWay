#!/usr/bin/python3
import pandas as pd
from sys import argv

script, text, max_freeq = argv
max_freeq = int(max_freeq)

df = pd.read_csv(text)
df1 = df[df['Freq'] >= max_freeq]
df1.to_csv('select_word',columns=['Word'],header=None,index=None)
