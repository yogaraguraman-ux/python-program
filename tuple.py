tuple_1=(24,34,56,67)
print(tuple_1)
print(type(tuple_1))

tuple_2=(5,)
print(type(tuple_2))

tuple_3=(12,45,67,88,89,90)
for data in tuple_3:
    print(data,end=" ")
print()
i=0
while i <len(tuple_3):
    print(tuple_3[1],end=" ")
    i+=1
print()
tuple_4=(1,2,3,4,5)
print(tuple_4.count(3))
print(tuple_4.index(4))
print(len(tuple_4))
print(sum(tuple_4))
print(min(tuple_4))
print(max(tuple_4))
tuple_7=(10,20,30,10,20,40)
for i in tuple_7:
    if tuple_7.count(i) > 1:
        if tuple_7.index(i) == tuple_7.index(i):
            print(i)
