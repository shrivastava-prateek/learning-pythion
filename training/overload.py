class overload:
    def __init__(self):
        pass
    def add(self,i):
        return i
    def add(self,i,j):
        return i+j

obj=overload()
a=obj.add(1)
print a
b=obj.add(1,2)
print b
    
