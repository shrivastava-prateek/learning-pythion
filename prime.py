def checkPrime(x):
    i=2
    j=0
    if x==2 or x==3 :
       return j
    else :
       while(i<=(int(x**(1.0/2.0)))):
           if x%i==0:
                 j=j+1
           i+=1
       return j

