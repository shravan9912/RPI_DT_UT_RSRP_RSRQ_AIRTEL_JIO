import datetime
import string
import csv 
import speedtest   
import Tkinter 
import pdfkit
import os

# field names 
fields = ['Start Time', 'End Time', 'Longitude', 'Latitude','altitude','download','upload','delay'] 
'''def time():
    current_time=datetime.datetime.now()
    return current_time'''

def dsusonly():
    print("Started ds us")
    st=current_time=datetime.datetime.now()
    wifi  = speedtest.Speedtest()
    ds=(wifi.download()/1024)/1024
    us=(wifi.upload()/1024)/1024    #print("Wifi Download Speed is ", wifi.download())
    delay=wifi.results.ping
    et=current_time=datetime.datetime.now()
    filename = "dsus_entry.csv"
    with open(filename, 'a') as csvfile:
        # creating a csv writer object 
          csvwriter = csv.writer(csvfile) 
          rows=[[st,et,'Airtel','NA','NA',us,ds,delay]]
          csvwriter.writerows(rows)
          print("Completed ds us")
          print("----------------------")
    #return st,et,us,ds,delay

top = Tkinter.Tk()
# Code to add widgets will go here...
#B = Tkinter.Button(top, text ="Speed Test", command = dsus)
#B.pack()
B = Tkinter.Button(top, text ="Speed Test Only", command = dsusonly)
B.pack()
top.mainloop()