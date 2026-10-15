numbers={1,2,3,6,4,3,2}
print (numbers)
names={"abilash","basha","david","elago"}
print(names)
empty_set=set()
empty_set={42,32,45}
print(empty_set)
nums1={10,20,30}
print(nums1)
nums1.add(50)
print(nums1)
nums1.update([60,70,80])
print(nums1)
nums2={1,2,3,4,5,5,6,7,1,2}
unique_set=set(nums2)
print(unique_set)
num3={50,70,40,80,100}
num3.remove(50)
print(num3)
num3.discard(100)
print(num3)
num3.remove(70)
print(num3)
num3.discard(70)
print(num3)
num3.clear()
print(num3)
num4={1,2,3,4,5,6,7,8,9}
for value in num4:
    print(value,end=" ")
print()
a={1,2,3,1}
b={3,4,5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))


student={
    "name":"naveen",
    "age":20,
    "mark":420,
    "dept":"ece"
}
print(student)
print(student["name"])
print(student["age"])
print(student.get("mark"))
print(student.get("city","not applicable"))
student["mark"]=441
print(student)
student["city"]="pondy"
print(student)
student.pop("age")
print(student)

for a,b in student.items():
    print(a,":",b)
print()

name="naveen"
dept="python"
print(name)
print(dept)
print(dept[0])
print(dept[1])
print(dept[-1])
print(dept[:3])
print(dept[2:6])
print(dept[::-1])
a="python"
a="i"+a[1:]
print(a)
print(len(a))
for ch in a:
    print(ch,end=" ")
print()
text="java programing"
print(text.upper())
print(text.lower())
print(text.replace("java","python"))
print(text.count("a"))
print(text.find("programing"))
print(text.find("c"))
print(text.startswith("java"))
print(text.endswith("programming"))

text1="                        java programming       "
print(text1.strip())
text2="java python node.js"
course=text2.split()
print(course)
text3=["python","java","c++"]
text4=",".join(text3)
print(text4)

def greet():
    print("hi jagan")
greet()
greet()

def addition(a,b):
    print(a+b)

addition(5,6)
addition(100,200)
addition(400,500)
def multiplication(a,b,c):
    return a*b*c
result=multiplication(5,5,5)
print(result)

def college():
    message="hello"
def google():
    print(message)
google()