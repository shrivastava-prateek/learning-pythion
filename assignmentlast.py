import urllib
import cx_0racle
#a_url='http://www.google.com'
#data=urllib.urlopen(a_url).read()
#print data

con = cx_Oracle.connect('pythonhol/welcome@127.0.0.1/orcl')
print con.version

con.close()

