# Import libraries
from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os
import csv
import pandas as pd

def pdftotxtt(filenames):
        # Path of the pdf
    PDF_file = str("jio_pdf/"+filenames+".pdf")

    '''
    Part #1 : Converting PDF to images
    '''

    # Store all the pages of the PDF in a variable
    pages = convert_from_path(PDF_file, 500)

    # Counter to store images of each page of PDF to image
    image_counter = 1

    # Iterate through all the pages stored above
    for page in pages:

        # Declaring filename for each page of PDF as JPG
        # For each page, filename will be:
        # PDF page 1 -> page_1.jpg
        # PDF page 2 -> page_2.jpg
        # PDF page 3 -> page_3.jpg
        # ....
        # PDF page n -> page_n.jpg
        filename = "page_"+str(image_counter)+".jpg"
        
        # Save the image of the page in system
        page.save(filename, 'JPEG')

        # Increment the counter to update filename
        image_counter = image_counter + 1

    '''
    Part #2 - Recognizing text from the images using OCR
    '''
    # Variable to get count of total number of pages
    filelimit = image_counter-1

    # Creating a text file to write the output
    outfile = str("jio_txt/"+filenames+".txt")

    # Open the file in append mode so that
    # All contents of all images are added to the same file
    f = open(outfile, "a")

    # Iterate from 1 to total number of pages
    for i in range(1, filelimit + 1):

        # Set filename to recognize text from
        # Again, these files will be:
        # page_1.jpg
        # page_2.jpg
        # ....
        # page_n.jpg
        filename = "page_"+str(i)+".jpg"
            
        # Recognize the text as string in image using pytesserct
        text = str(((pytesseract.image_to_string(Image.open(filename)))))

        # The recognized text is stored in variable text
        # Any string processing may be applied on text
        # Here, basic formatting has been done:
        # In many PDFs, at line ending, if a word can't
        # be written fully, a 'hyphen' is added.
        # The rest of the word is written in the next line
        # Eg: This is a sample text this word here GeeksF-
        # orGeeks is half on first line, remaining on next.
        # To remove this, we replace every '-\n' to ''.
        text = text.replace('', '')	

        # Finally, write the processed text to the file.
        f.write(text)

    # Close the file after writing all the text.
    f.close()
    return filenames

def readtext(filenames,filenames2):
    txtfile=str("jio_txt/"+filenames1+".txt")
    ilist=[]
    k=1
    with open(txtfile) as file:
        for item in file:
            if (item != " \n") and (item != "\n") and (item != "\x0c"):
               ilist.append(str(k))
               ilist.append(item)
               k=k+1
    with open(txtfile) as file:
        for item in file:
            if (item != " \n") and (item != "\n") and (item != "\x0c"):
               ilist.append(str(k))
               ilist.append(item)
               k=k+1
  
           # print(item)
    #print(ilist)
    for idx, ele in enumerate(ilist):
            ilist[idx] = ele.replace('\n', '')

    #print(ilist)
    init = iter(ilist)  
    res_dct = dict(zip(init, init))  
    print(res_dct)
    print("")
    #print(res_dct['29'], res_dct['30'],res_dct['32'],res_dct['33'],res_dct['34'],res_dct['35'],res_dct['36'])
    signallist=[res_dct['29'], res_dct['30'],res_dct['32'],res_dct['33'],res_dct['34'],res_dct['35'],res_dct['36'],res_dct['66'], res_dct['67'],res_dct['68'],res_dct['69'],res_dct['70'],res_dct['71'],res_dct['72']]
    return signallist

def finalcsv(finallist):
 with open('final_jio_csv.csv', 'a') as f:
     #using csv.writer method from CSV package
      write = csv.writer(f)      
    #write.writerow(fields)
      write.writerow(finallist)


with open('dsus_entry.csv', newline='') as file:
    reader = csv.reader(file)
    print("Reader")
    print(reader)
    speedlist = list(map(list, reader))
results = pd.read_csv('dsus_entry.csv')
linec= len(results)
i=0
while i < linec:
 filenames1=str(speedlist[i][0])
 filenames2=str(speedlist[i][1])
 pdftotxtt(filenames1)
 pdftotxtt(filenames2)
 signallist=readtext(filenames1,filenames2)
 finallist=[]
 for ky in speedlist[i]:
   finallist.append(ky)
 for xy in signallist:
   finallist.append(xy)

 finalcsv(finallist)
 i=i+1



