#shravan
import pandas as pd
import matplotlib.pyplot as plt
import pandasql as ps
import numpy as np
#from pandasql import sqldf
import pandas as pd
# read specific columns of csv file using Pandas
df = pd.read_csv("final_Jio_csv.csv", usecols = ['rsrq_1','download_speed','altitude']) 
print(df) 
subjects=list(df.altitude.unique())  
# Create a list of data
# to be represented in y-axis
stress=list(df.download_speed)
# Create second list of data to be represented in y-axis
grades=list(df.rsrq_1.str.replace('[^0-9-]',''))
gd=list(np.float_(grades))
df["rsrq_1"]=gd
print(df)
col1=[]
#col2=[]
q=0
while q<=8:
 a=ps.sqldf("select rsrq_1 from df where altitude="+str(q))
 print(float(a.mean()))
 col1.append(float(a.mean()))
 #col2.append(float(b.mean()))
 q=q+1
print(col1)
#print(col2)
print(subjects)
#ax = plt.gca()
df_days_calories = pd.DataFrame(
    { 'altitude' : subjects , 
     'RSRQ': col1 ,})
  
ax = plt.gca()
  
#use plot() method on the dataframe
df_days_calories.plot( x = 'altitude' , y = 'RSRQ', ax = ax )
#df_days_calories.plot( x = 'altitude' , y = 'upload_speed' , ax = ax )
plt.show()
