
num=int(input("enter  number:"))
total=0
for i in range(1,num+1):
    total=total+i
print(total)
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
totals=0
for i in range(num1,num2+1):
    if i%2==0:
        totals+=i
print(totals)