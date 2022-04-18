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

def signalonly():
    print("Signal test started")
    st=current_time=datetime.datetime.now()
    ststr=str(st)
    pdfkit.from_url('http://192.168.1.1/',"signaltestonly/"+ststr+"start.pdf")
    et=current_time=datetime.datetime.now()
    etstr=str(et)
    pdfkit.from_url('http://192.168.1.1/index.html',"signaltestonly/"+etstr+"end.pdf")
    print("Signal test Completed")
    print("----------------------")
    #return st,et,us,ds,delay

top = Tkinter.Tk()
# Code to add widgets will go here...
#B = Tkinter.Button(top, text ="Signal Test Only", command = dsus)
#B.pack()
B = Tkinter.Button(top, text ="Signal Test Only", command = signalonly)
B.pack()
top.mainloop()