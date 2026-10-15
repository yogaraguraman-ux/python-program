for i in range(5, 0, -1):
    print(" " * (5 - i) + "*" * i)
for i in range(2, 6):
    print(" " * (5 - i) + "*" * i)
print()
import math
from math import sqrt
import calculator
addition=lamda a ,b:a+b
print (addition(4,3))
square=lamda a=a*a
print(square(5))

print(math.sqrt(25))
print(math.factorial(5))
print(math.pi)
print (calculator.multi(5,5,5))
try:
    a= int(input())
    b=int(input())
    c=a//b
    print(c)
except zerodivisionerror:
    print("plese enter positive number")
except valueerror: 
    print("enter integer only")
finally:
    print("java programming")
