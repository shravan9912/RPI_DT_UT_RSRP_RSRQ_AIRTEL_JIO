#shravan
import pandas as pd
import matplotlib.pyplot as plt
import pandasql as ps
#from pandasql import sqldf
# importing the module
import pandas as pd
# read specific columns of csv file using Pandas
df = pd.read_csv("final_Jio_csv.csv", usecols = ['upload_speed','download_speed','altitude']) 
print(df) 
# Create a list of data
# to be represented in x-axis
#subjects = [ 'Math' , 'English' , 'History ',
            #'Chem' , 'Geo' , 'Physics' , 'Bio' , 'CS' ]
subjects=list(df.altitude.unique())  
# Create a list of data
# to be represented in y-axis
#stress = [ 9, 3 , 5 , 1 , 8 , 5 , 10 , 2 ]
stress=list(df.download_speed)
# Create second list of data to be represented in y-axis
#grades = [ 15, 10 , 7 , 8 , 11 , 8 , 17 , 20 ]
grades=list(df.upload_speed)
# Create a dataframe using the two lists
#df_days_calories = pd.DataFrame({'altitude':df.altitude,'upload_speed': df.upload_speed,'download_speed': df.download_speed})
col1=[]
col2=[]
q=0
while q<=8:
 a=ps.sqldf("select download_speed from df where altitude="+str(q)) 
 b=ps.sqldf("select upload_speed from df where altitude="+str(q))
 print(a.mean())
 col1.append(float(a.mean()))
 col2.append(float(b.mean()))
 q=q+1
print(col1)
print(col2)
print(subjects)
#ax = plt.gca()
df_days_calories = pd.DataFrame(
    { 'altitude' : subjects , 
     'download_speed': col1 , 
     'upload_speed': col2})
  
ax = plt.gca()
  
#use plot() method on the dataframe
df_days_calories.plot( x = 'altitude' , y = 'download_speed', ax = ax )
df_days_calories.plot( x = 'altitude' , y = 'upload_speed' , ax = ax )
plt.show()
