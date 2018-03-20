class queue:
    a=1
    def __init__(self):
        self.front=-1
        self.rear=-1
        self.list=[]



    def enqueue(self,element):
        if self.front==-1 and self.rear==-1:
            self.front=self.front+1
        self.list.append(element)
        self.rear=self.rear+1

    def dequeue(self):
        a=2
        print a
        self.list.remove(self.front)
        self.front=self.front+1

    def test(self):
        print queue.a
        obj=queue()
        obj.b=5
        print obj.b
        print "adding element 1,4,6,8,0"
        obj.enqueue(1)
        print obj.list
        obj.enqueue(4)
        print obj.list
        obj.enqueue(6)
        print obj.list
        obj.enqueue(8)
        print obj.list
        obj.enqueue(0)
        print obj.list
        print "deleting elements"
        obj.dequeue()
        print obj.list
        obj.dequeue()
        print obj.list

obj1=queue()
obj1.test()
        
            
        
