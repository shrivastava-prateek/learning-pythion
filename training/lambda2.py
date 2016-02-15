
def make_inc(n):
    return lambda x:x+n

f1= make_inc(1)
f2= make_inc(2)
print f1(50)
n=5
def my_func(make_inc,b):
    a=make_inc(n)
    return a*b

print my_func(make_inc(n),4)
    
