#x =  input(" print the value of x ")
#print x

x=[1,2,3]
y=[1,2,3]
print x==y
print x is y
x=0
y=0
print x==y
print x is y

z=6
print y or x and z

time = int(raw_input("please enter the time"))
time_anot=(str(time) + "AM") if time <=12 else ((str(time-12)) + "PM")
print time_anot
