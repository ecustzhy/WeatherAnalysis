import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
df_ferrara = pd.read_csv('ferrara_270615.csv')
df_milano = pd.read_csv('milano_270615.csv')
df_mantova = pd.read_csv('mantova_270615.csv')
df_ravenna = pd.read_csv('ravenna_270615.csv')
df_torino = pd.read_csv('torino_270615.csv')
df_asti = pd.read_csv('asti_270615.csv')
df_bologna = pd.read_csv('bologna_270615.csv')
df_piacenza = pd.read_csv('piacenza_270615.csv')
df_cesena = pd.read_csv('cesena_270615.csv')
df_faenza = pd.read_csv('faenza_270615.csv')
x=df_milano['day']
y=df_milano['temp']
x2=df_mantova['day']
y2=df_mantova['temp']
x3=[parser.parse(a) for a in x2]
x1=[parser.parse(a) for a in x]
fig,ax=plt.subplots()
plt.xticks(rotation=70)
hour=mdates.DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(hour)
ax.plot(x1,y,'r',x3,y2,'g')
plt.show()
