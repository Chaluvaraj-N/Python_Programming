#WAP to implement linear search algorithm without using function

def createIntarray():
    print("enter the values into the int to be created: ")
    l1=[]
    while True:
        try:
            n=int(input("enter value: "))
            l1.append(n)
        except Exception as e:
            return l1
arr=createIntarray()
target=int(input("enter a num to search : "))
flag,index=False,-1
for i in range(0,len(arr)):
    if target == arr[i]:
        flag = True
        index = i
        break
print("original arr: ",arr)
if flag:
    print(f"the {target} element is found at index:{index}")
else:
    print(f"the {target} element is not found")