ports = (21,23,[80,443],3306,5432)
proto = ['ftp','telnet',('http','https'),'mysql','postgress']
server = 'brahma.irctc.co.in'
print 'ftp' in proto
'ftp' in proto


#ports[1]=22 can not be reassigned
ports = ports+ (2048,22) #creating a new reference
proto[1]='TELNET'
proto.append('nfs')
proto.append('ssh')
print proto

proto.insert(2,'smtp')
print proto

print server[2:-4]
             
print server.count('c',11,12)
print server.count('c')
print server
#server.pop(0)
print server

l1=[1,1,1,2,2,2,3,3,4,2]
l2=set(l1)
print l2

print dir(set)

#update l2

