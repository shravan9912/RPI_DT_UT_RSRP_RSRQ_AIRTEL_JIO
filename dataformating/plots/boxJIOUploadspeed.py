import pandas as pd
import numpy as np
import pandasql as ps
import matplotlib.pyplot as plt
df = pd.read_csv("final_Jio_csv.csv", usecols = ['upload_speed','download_speed','altitude']) 
print(df) 
q=0
d={}
while q<=7:
 a=ps.sqldf("select upload_speed from df where altitude="+str(q))
 print(a["upload_speed"].tolist())
 b=a["upload_speed"].tolist()
 d.update({q:b})
 #b=list(a)
 print(a) 
 q=q+1
#df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
#b=list(a)
#print(b)
print(df)
print(d)
df1 = pd.DataFrame(d)
print(df1)  
df1.plot.box(grid='True')
#plt.axis([None, None, 0, 40])
plt.show()
