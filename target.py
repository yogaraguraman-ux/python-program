nums=[]
n=int(input("enter  n:"))
for i in range(n):
    data=int(input("enter data:"))
    nums.append(data)
target=int(input("enter target:"))
found=False
for i in range(n):
    for j in range(i+1,n):
        if nums[i]+nums[j]==target:
            print(f"{i},{j}")
            fount=True
            break
    if found:
        break
if not found:
    print("-1,-1")
print()
