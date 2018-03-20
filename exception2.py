try: 
    raise Exception('spam', 'eggs') 
except Exception, inst:
    print type(inst) 
    print inst.args 
    print inst 
    x, y = inst 
    print 'x =', x 
    print 'y =', y 
    #^D
