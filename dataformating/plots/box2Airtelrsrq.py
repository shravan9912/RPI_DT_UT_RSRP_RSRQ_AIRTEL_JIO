import pandas as pd
import numpy as np
import pandasql as ps
import matplotlib.pyplot as plt
df = pd.read_csv("final_airtel_csv.csv", usecols = ['rsrq_1','download_speed','altitude'])
grades=list(df.rsrq_1.str.replace('[^0-9-]',''))
gd=list(np.float_(grades))
df["rsrq_1"]=gd 
print(df) 
q=0
d={}
while q<=7:
 a=ps.sqldf("select rsrq_1 from df where altitude="+str(q))
 print(a["rsrq_1"].tolist())
 b=a["rsrq_1"].tolist()
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
plt.show()
