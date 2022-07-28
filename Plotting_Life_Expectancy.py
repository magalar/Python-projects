import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/Users/masteruser/Desktop/dataset/gapminder_full.csv")
df_2007 = df[df["year"]==2007].sort_values('population', ascending=False).reset_index(drop=True)

print(df_2007.head())

# Store urban rate as a numpy array: np_pop
np_pop = np.array(df_2007.population)
# Double np_pop
np_pop2 = np_pop*2

#Scatter plot, log scale
fix, ax = plt.subplots(figsize =(10, 7))
sns.scatterplot(data=df_2007, x="gdp_cap", y = "life_exp", hue = "continent",  size = np_pop2, sizes=(20,1000), alpha = 0.8, legend = True, ax =ax)

xlab = "Income - GDP per Person in US dollars (log scale)"
ylab = "Life Expectancy (years)"
title = "Global Life Expectancy- 2007"

ax.set(xscale = "log", xlabel=xlab, ylabel=ylab, title=title)
ax.grid(True)

#Replace the x-tick values 1000, 10000 and 100000 with 1k, 10k and 100k.
plt.xticks([1000, 10000, 100000],["1k", "10k", "100k"])

offset = 1
for idx, (x, y, s, c) in df_2007.iloc[:15, [5, 4, 2, 0]].iterrows():
    ax.text(x+offset, y, c, va='center', fontsize=8)

plt.show()
