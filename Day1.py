#6/8/2023
a = input("Enter first number: ")
b = input("Enter second number: ")
c = input("Enter third number: ")
print("first number = " + a)
print("second number = " + b)
print("third number = " + c)

largest = 0

if a > b and a > c:
    largest = a
if b > a and b > c:
    largest = b
if c > a and c > b:
    largest = c

print(largest, "is the largest of three numbers.")