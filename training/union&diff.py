hash1 = {'1':'a','2':'b','3':'c','4':'d'}
hash2 = {'1':'a','5':'c','4':'e'}
d={}
for (k,v) in hash1.items():
    t=[]
    c=0
    for (k1,v1) in hash2.items():
        if k1==k:
            if v1==v:
                d[k]=v1
                c=1
                break
            else:
                t=[v,v1]
                d[k]=t
                c=1
    if d.has_key(k) and c==1:
        continue
    else:
        d[k]=v
for(k,v) in hash2.items():
   if d.has_key(k):
        continue
   else:
        d[k]=v
print d

#diff
d1={}
for (k,v) in hash1.items():
    c=0
    for (k1,v1) in hash2.items():
        if k1==k:
            if v1==v:
                c=1
                continue
    if c==1:
        continue
    else:
        d1[k]=v
print d1
