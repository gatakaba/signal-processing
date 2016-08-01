#coding:utf-8
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

l=[]
for line in open("log.txt"):
    s = line.split("|")
    s = map(lambda x:x.rstrip(),s)
    s = map(lambda x:re.search(".* = (.*)",x).group(1),s)
    s = map(float ,s)
    l.append(s)

l= np.array(l)
labels = ["AcX","AcY","AcZ" ,"Tmp","GyX","GyY ","GyZ"]
df= pd.DataFrame(l,columns=labels)

for label in labels:
    plt.title(label)
    plt.plot(df[label])
    plt.plot(pd.rolling_mean(df[label],11),linewidth=3)
    plt.savefig(label+".png")
    plt.clf()
