class Student:
    x=0 # class variable shared by evry object
    def __init__(self,n,a):
        self.full_name = n # instance variable 
        self.age = a       # instance variable
        self.__class__.x +=1
        self.roll = self.__class__.total
        
    def get_age(self):
        return self.age
