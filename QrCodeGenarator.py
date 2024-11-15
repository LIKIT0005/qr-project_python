# QR CODE GENARATOR
import qrcode as qr
import pandas as pd


def csvqr(csvdata):
    csvdata = pd.read_csv(inputfile)
    qrpng=qr.make(csvdata)
    qrpng.save(output+".png")
    return qrpng

def url(link):
    qrpng = qr.make(str(link))
    qrpng.save(output+".png")
    return qrpng

def textfile(textdata):
    with open(inputfile,"r") as file:
        textdata =file.read()
    qrpng = qr.make(textdata)
    qrpng.save(output+".png")
    return qrpng

def textqr(typeddata):
    qrpng = qr.make(typeddata)
    qrpng.save(output+".png")
    return qrpng


question = input("""what do you want to convert into a qr code chose from below
                                     [csvfile, url , textfile, text] :- """)

question = question.upper()

while True:
    if question == "CSVFILE" or question == "csvfile":
        answer = input("Enter the path of your CSV file :- ")
        inputfile = answer
        output = input("enter your qrname :-")
        csvqr(inputfile)
        print(" THANK YOU ")

    elif question == "URL" or question == "url":
        answer = input("Enter YOUR url :- ")
        if answer.startswith("https"):
            output = input("enter your qrname :- ")
            url(answer)
        else:
            print("""your url is not secured
                  use url starting with 'https' """)
        print(" THANK YOU ")

    elif question == "TEXTFILE" or question == "textfile":
        answer = input("Enter the path of your text file :- ")
        inputfile = answer
        output = input("enter your qrname :- ")
        textfile(inputfile)
        print(" THANK YOU ")

    elif question == "TEXT" or question == "text":
        answer = input("Enter the text you want to convert into a QR code :- ")
        typeddata = answer
        output = input("enter your qrname :- ")
        textqr(typeddata)
        print(" THANK YOU ")

    else:
        print("EXITING....")
        break
