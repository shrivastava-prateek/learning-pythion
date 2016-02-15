try:
    x=int(raw_input("please enter a number:"))
except ValueError:
    print "Oops!That was no valid number.Try again.."


import sys
try:
    f=open('output.txt');s=f.readline()
    i=int(s.strip())
    print i
except IOError,(errno,strerror):
    print "I/O error(%s): %s" %(errno,strerror)
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unexpected error:",sys.exc_info()[0]
    raise
