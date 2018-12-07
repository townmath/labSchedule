#by Jim Town 
#with help from: https://stackoverflow.com/questions/42748343/how-to-show-csv-file-in-a-grid/42748973
#and https://stackoverflow.com/questions/23901168/how-do-i-insert-a-jpeg-image-into-a-python-tkinter-window
#and https://stackoverflow.com/questions/25753632/tkinter-how-to-use-after-method
#and the letter C
import tkinter as tk
from PIL import ImageTk, Image
import csv
from datetime import datetime
import os
#print (datetime.now())
#print (datetime.now().strftime('%H'))

root = tk.Tk()
#all images shrunk to 150 pixels tall (or wide if it was rectangular)
#and given clear backgrounds
#scc image from https://www.scc.losrios.edu/styleguide/logos-marks/
#linux image: the copyright holder of this file allows anyone to use it for
#any purpose, provided that the copyright holder is properly attributed.
#Redistribution, derivative work, commercial use, and all other use is
#permitted.
#Attribution: lewing@isc.tamu.edu Larry Ewing and The GIMP
imgDict={}
imgDir="."
for fileName in os.listdir(imgDir):
   if fileName.endswith("png"):
      imgDict[fileName[:-4]]=ImageTk.PhotoImage(Image.open(imgDir+'\\'+fileName))

#open file
def loadSchedule():#oclock,dow):#testing
   curr=datetime.now().strftime('%H %a')
   oclock,dow=curr.lower().split(' ')  
   oclock=int(oclock)
   dow=dow[:2]
   with open("tutor.csv", newline = "") as file:
      reader = csv.reader(file)
      # r and c tell us where to grid the labels
      i=0
      for row in reader:
         #print(row)
         j=0
         good=(int(row[2])<=oclock and int(row[3])>oclock and dow in row[4].split(' '))
         if good:
            for col in row:
               if j<2:
               # i've added some styling
                  if i==0:#first row
                     font=("Times",24)
                     relief=tk.FLAT
                  else:
                     font=("Times",48)
                     relief=tk.RIDGE
                  label = tk.Label(root, width=10, height=2,
                                   text=col, relief=relief,
                                   font=font)
                  label.grid(row=i, column=j)
               elif j==5:
                  for image in col.split(' '):
                     print(image)
                     img=imgDict[image]#eval(image)
                     #img = ImageTk.PhotoImage(Image.open(path)) #only shows last image
                     label = tk.Label(root, image=img)
                     label.grid(row=i,column=j)
                     j+=1
               j+=1
            i+=1
   root.geometry("") #resizes the window to fit all of the children
   delay=1000*60*15 #milli/sec*sec/min*min = 15 minutes
   root.after(delay,loadSchedule)



if True:#__name__=="__main__":
   root.after(0,loadSchedule)
   #loadSchedule(oclock,dow)#testing
   #loadSchedule(13,'fr')#testing
   root.mainloop()
