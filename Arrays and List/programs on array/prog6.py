#WAP to implement linear search algorithm using function


def linear():
    l1=[]
    while True:
        try:
            n = int(input("enter num:"))
            l1.append(n)
        except Exception as e:
            return l1
def intarray(arr,target):
    for i in range(0,len(arr)):
        if target == arr[i]:
            return True,i
    return False, -1

arr = linear()
target = int(input("enter the target value to be find"))
flag, index = intarray(arr, target)

print("origanal values are: ",arr)

if flag:
    print(f"The {target} elemnt is found at index {index}")
else:
    print(f"{target} element is not found")