#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


# In[2]:


A = np.linspace(0, 1)
B = [x**2 for x in A]
C = [np.cos(2 * np.pi * x) for x in A]
S = [np.sin(2 * np.pi * x) for x in A]
E = np.random.rand(len(A)) / 20 + 0.1
df = pd.DataFrame([A, B, C, S, E], index=["x", "squarex", "$cos_x$", "sinx", "error"]).T


# In[3]:


plt.rcParams["mathtext.fontset"] = "stix"


# In[7]:


plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 15  # 適当に必要なサイズに
plt.rcParams['xtick.direction'] = 'in'  # in or out
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['axes.xmargin'] = 0.05
plt.rcParams['axes.ymargin'] = 0.05
plt.rcParams["legend.fancybox"] = False  # 丸角OFF
plt.rcParams["legend.framealpha"] = 1  # 透明度の指定、0で塗りつぶしなし
plt.rcParams["legend.edgecolor"] = 'black'  # edgeの色を変更


# In[10]:


for i, coln in enumerate(df.columns):
    plt.plot(df.index, df[coln], label=coln)
plt.xlabel("hoge")
plt.ylabel("huga")
plt.title("piyo")
plt.minorticks_on()
plt.grid(which="major", color="black", alpha=0.4)
plt.grid(which="minor", color="gray", linestyle=":")
plt.show()


# In[14]:


for i, coln in enumerate(df.columns):
    plt.scatter(df.index, df[coln], label=coln,
                s=5)  # sは点のサイズ
plt.xlabel("hoge")
plt.ylabel("huga")
plt.title("piyo")
plt.minorticks_on()
plt.grid(which="major", color="black", alpha=0.4)
plt.grid(which="minor", color="gray", linestyle=":")
plt.savefig("hoge", dpi=300)  # dpiは解像度。300だとちょっと大きい。
plt.show()
