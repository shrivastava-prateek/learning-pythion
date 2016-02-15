import re
pat1 = re.compile('(abc)+')
if pat1.search('abcabc'):
   print "it matched"
else:
   print "not matched"
