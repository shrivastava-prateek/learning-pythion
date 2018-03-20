f=open("output.txt","w")
f.write("hello")
f.close()


f = open("output.txt")
print f.readline()
print "remaining file"
print f.read()
f.close()


file = open('output.txt', 'rb')
while True:
     chunk = file.read(10)
     if not chunk: 
           break
     print chunk

