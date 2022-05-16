import datetime
import string
import csv 
import speedtest   
import Tkinter 
import pdfkit
import os
while True:
    print("Started ds us")
    st=current_time=datetime.datetime.now()
    wifi  = speedtest.Speedtest()
    ststr=str(st)
    pdfkit.from_url('http://192.168.1.1/index.html',"signal/"+ststr+".pdf")
    file_size = os.path.getsize("signal/"+ststr+".pdf")
    int(file_size)
    while file_size < 20048:
       pdfkit.from_url('http://192.168.1.1/index.html',"signal/"+ststr+".pdf")
       file_size = os.path.getsize("signal/"+ststr+".pdf")
    ds=(wifi.download()/1024)/1024
    us=(wifi.upload()/1024)/1024    #print("Wifi Download Speed is ", wifi.download())
    delay=wifi.results.ping
    et=current_time=datetime.datetime.now()
    etstr=str(et)
    pdfkit.from_url('http://192.168.1.1/index.html',"signal/"+etstr+".pdf")
    file_size = os.path.getsize("signal/"+etstr+".pdf")
    int(file_size)
    while file_size < 20048:
       pdfkit.from_url('http://192.168.1.1/index.html',"signal/"+etstr+".pdf")
       file_size = os.path.getsize("signal/"+etstr+".pdf")
    filename = "dsus_entry.csv"
    with open(filename, 'a') as csvfile:
        # creating a csv writer object 
          csvwriter = csv.writer(csvfile) 
          rows=[[st,et,'Airtel','NA','NA',us,ds,delay]]
          csvwriter.writerows(rows)
          print("Completed ds us")
          print("----------------------")
    #return st,et,us,ds,delay
