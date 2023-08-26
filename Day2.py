#7/8/2023
a=int(input("Number of elements in the array:"))
#b=int(input("Number of elements in the array:"))
n=list(map(int, input("elements of array:-").strip().split()))
#n=list("elements of array:-",{a},{b})
print(n)
#how we write program in python that can user write array and check
#the sum two numbers in array equal t number from programmars
t = 5
print("t : " ,t)
for i in list(n):
    sum = i 
print(sum)
if(sum == t):
  print("It equal to t", sum)
else:
  print("It is not equal")
