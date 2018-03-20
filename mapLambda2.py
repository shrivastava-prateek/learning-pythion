sem1= [12,11,13,10,9]
sem2=[14,18,15,11,13]
print map(lambda x,y:x+y,sem1,sem2)

print map(lambda x,y:x if x>y else y,sem1,sem2)
marks_tup = zip(sem1,sem2)

print filter(lambda (x,y):x<y,zip(sem1,sem2))

ports = (21,23,80,443,3306,5432)
proto = ['ftp','telnet','http','https','mysql','postgress']

dict={}
i=0
for k in proto:
        dict[k]=ports[i]
        i=i+1

print dict

#dict2={}
#print dict2(zip(proto,ports))
