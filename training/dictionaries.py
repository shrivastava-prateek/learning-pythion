user = {'name':'sanchit',
        'pass':'abc123',
        'pan':'abcdef'}
print user['name']
print user.has_key('uid')
print user.keys()
print user.values()
print user
print user.items()
#assignment 1
x= raw_input("enter the key value")
if x in user.keys():
    print "key is present"
    print x,"=>",user[x]
else:
    print "key is not present"
#assignment 2
y=raw_input("enter the value")

for key in user.keys():
    if user[key]==y:
       print key,"=>",user[key]


