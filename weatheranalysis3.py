import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from sklearn.svm import SVR
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
data1=pd.DataFrame({'tempmax':max_temp,'tempmin':min_temp,'dist':dist},index=list(range(10)))
data=data1.sort_values(by='dist').reset_index(drop=True)
dist1=np.array(data['dist'][:5])
dist11=[[x] for x in dist1]
dist2=np.array(data['dist'][5:10])
dist22=[[x] for x in dist2]
max_temp1=np.array(data['tempmax'][:5])
max_temp2=np.array(data['tempmax'][5:10])

svr1=SVR(kernel='linear', C=1e3)
svr2=SVR(kernel='linear', C=1e3)
svr1.fit(dist11,max_temp1)
svr2.fit(dist22,max_temp2)
xp1 = np.arange(10,80,10).reshape((7,1))
xp2 = np.arange(100,450,50).reshape((7,1))
yp1 = svr1.predict(xp1)
yp2 = svr2.predict(xp2)
fig, ax=plt.subplots()
ax.plot(xp1, yp1, c='b', label='Strong sea effect')
ax.plot(xp2, yp2, c='g', label='Light sea effect')
ax.scatter(xp1,yp1,label='data')
plt.legend(loc='best')
plt.show()
