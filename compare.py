n1=int(input("enter n1:"))
n2=int(input("enter n2:"))
n3=int(input("enter n3:"))

if n1 > n2 and n1 > n3:
    print("n1 is the greater")
elif n2 > n1 and n2 > n3:
    print("n2 is the  greater")
elif n3 > n1 and n3 > n2:
    print("n3 is the  greater")
else:
    print("Two or more numbers are equal")