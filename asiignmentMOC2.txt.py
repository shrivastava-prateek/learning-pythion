l1=['a','b']
l2=['c','d']
l3=[]
for i in l2:
     l=[j+i for j in l1]
     l3.append(l)

print l3
