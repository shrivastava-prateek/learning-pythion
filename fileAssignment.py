import sys
import os
f=0
def create():
    global f
    f=open("C:\Users\Administrator\Desktop\python\python_subjective_assignment2.txt",'w+')
    print "file created successfully\n"

def display():
    global f
    f.seek(0,0)
    for line in f:
        print line
        print "\n"
    print "End of File\n"

def edit():
    global f
    while True:
         s=raw_input("Enter your text:\n")
         f.write(s)
         s1=raw_input("Enter Y for more or else  N :\n")
         if s1=="y" or s1=="Y":
             continue
         else:
             break
    print "File edited successfully\n"

def quit():
    global f
    if f.closed:
        sys.exit()
    else:
        print "first save and close the file\n"

def delete():
    global f
    if f.closed:
        os.remove("C:\Users\Administrator\Desktop\python\python_subjective_assignment2.txt")
        print "File Deleted successfully\n"
    else:
        print "please close the file first\n"

def save():
    global f
    f.flush()
    f.close()
    print "file saved and closed successfully\n"

while True:
    print "1.Create file \n2.Edit file \n3.Display file \n4.Save & Close \n5.Delete file \n6.Quit \n"
    i=input("Press 1,2,3,4,5 or 6 :\n")
    if i==1:
        create()
    elif i==2:
        edit()
    elif i==3:
        display()
    elif i==4:
        save()
    elif i==5:
        delete()
    elif i==6:
        quit()
    else:
        print "Enter in between 1-5 only\n"

