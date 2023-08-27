#13/8/2023
x=int(input("Enter the time you reach: "))

t=30
if(x==t):
    print("You reach office exactly in 30 minutes")
elif(x<t):
   print("You reach office 30 minutes  early")
else:
   y = x-t
   print("You reach office ",{ y}, "minutes  late") 