import re
pat1=re.compile('^([a-zA-Z])+([a-zA-Z0-9])(_)?([a-zA-Z0-9])+@(gmail|yahoo).(com|in)')
if pat1.search('k7_88hjk@gmail.com'):
     print 'y'
else:
     print 'no' 
