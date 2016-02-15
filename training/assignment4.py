s = "aba"
s1 ="aba"
l=[]
l.extend(s1)
l.reverse()
s3=reduce(lambda x,y:x+y,l)
if s==s3:
    print "palindome"
else:
    print "not palindrome"
