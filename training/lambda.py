f=lambda x:x*x
print f(12)

def applier(f):
    return lambda x:f(f(x))
def square(x):
    return x*x
quad = applier(square)
print quad(4)

def square(x):
    return x*x

def twice(f):
    return lambda x:f(f(x))

quad= twice(square)

print quad(5)
