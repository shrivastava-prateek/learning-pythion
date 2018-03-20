import re
'''
pat1 = re.compile('^home')   #begining of line
if pat1.search('home awaits'):
   print "matched"
else :
   print "not matched"

pat2 = re.compile('home$')   #end of line
if pat2.search(' heya home'):
   print "matched"
else :
   print "not matched"
'''
pat3 = re.compile('/w+@/w+(.com)$')   #end of line
if pat3.search('prateek@gamil.com'):
   print "matched"
else :
   print "not matched"
