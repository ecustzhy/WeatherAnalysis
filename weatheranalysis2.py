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

max_temp=[df_ferrara['temp'].max(),df_milano['temp'].max(),df_mantova['temp'].max(),df_ravenna['temp'].max(),
          df_torino['temp'].max(),df_asti['temp'].max(),df_bologna['temp'].max(),df_piacenza['temp'].max(),
          df_cesena['temp'].max(),df_faenza['temp'].max()]
min_temp=[df_ferrara['temp'].min(),df_milano['temp'].min(),df_mantova['temp'].min(),df_ravenna['temp'].min(),
          df_torino['temp'].min(),df_asti['temp'].min(),df_bologna['temp'].min(),df_piacenza['temp'].min(),
          df_cesena['temp'].min(),df_faenza['temp'].min()]
dist=[df_ferrara['dist'][0],df_milano['dist'][0],df_mantova['dist'][0],df_ravenna['dist'][0],
          df_torino['dist'][0],df_asti['dist'][0],df_bologna['dist'][0],df_piacenza['dist'][0],
          df_cesena['dist'][0],df_faenza['dist'][0]]
fig,ax=plt.subplots()
ax.plot(dist,max_temp,'ro')
ax.scatter(dist,min_temp)
plt.show()



