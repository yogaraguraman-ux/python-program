n=int(input("enter a number:"))
while not(n>=0 and n<10):
    sum=0
    while n!=0:
        rem=n%10
        sum=sum+rem
        n=n//10
    n=sum
else:
    print(n)

