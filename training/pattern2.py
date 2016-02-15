import re
pat1 = re.compile('ba?b')
if pat1.search("baab"):
     print "it matched"
else:
     print " not matched"


#import re
pat1 = re.compile('^\d{8,10}$')
if pat1.search("4444444444"):
     print "it matched"
else:
     print " not matched"

pat1 = re.compile('^(\+91)?\d{10}$')
if pat1.search("7415201766"):
     print "it matched"
else:
     print " not matched"

pat1 = re.compile('[aeiou]')
if pat1.search("who"):
     print "it matched"
else:
     print " not matched"

pat1 = re.compile('in$|jp$|uk$')
if pat1.search("yahoo.co.in.ot"):
     print "india server"
else:
     print "foreign server"
