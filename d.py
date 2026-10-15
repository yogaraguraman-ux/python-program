list_1=[24,56,78,9,0,23,23]
list_2=["jagan","kumar","navin","praveen"]
list_3=["navin",18,"M",9.8,"rgcet","true"]
print(list_1)
print(list_2)
print(list_3)
print(type(list_1))
list_4=[10,20,30,40]
print(list_4)


numbers=[]
n=int(input())
for i in range(n):
    data=int(input())
    numbers.append(data)
    print(numbers)


list_5=[1,2,3,4,5]
print(list_5)

for data in list_5:
    print(data,end="")
    print()
    i=0 #1<5
    while i<len(list_5):
        print(list_5[i],end=" ")
        i+=1
        print()

list_6=[1,2,3,4,5]
list_6.append(6)
list_6.append(7)
print(list_6)    
list_6.insert(0,1000)
print(list_6)

list_7=[10,20,30,40,20,30]
list_7.remove(30)
print(list_7)
list_7.pop()
print(list_7)
list_7.clear()


print("index")
list_7=[10,20,30,40,20,30]
print(list_7[4])
print(list_7[-4])

#list slicing 
nums=[10,20,30,40,50,60]
print(nums[1:4])
print(nums[:3])
print(nums[::2])
print(nums[-3:])
print(nums[::-1])
print(nums[::])

nums_1=[10,30,40,10]
print(10 in nums_1)
print(nums_1.count(10))
print(nums_1.index(30))


nums_2=[32,78,12,0,-9]
nums_2.sort()
print(nums_2)
nums_2.sort(reverse=true)
print(nums_2)

nums_3=[4,3,2,1]
nums_3.reverse()
print(nums_3)

num_4=[10,20,367,74,845,6372,83939]
print(num_4)
print(sum(nums))