#wap to print merge sort using inbuild functions
 
def createIntArr():
    l1=[]
    while True:
        try:
            n = int(input("enter valu: "))
            l1.append(n)
        except Exception as e:
            return l1

def mergealternate(arr1, arr2):
    odd = 1
    for j in range(0,len(arr2)):
        arr1. insert(odd, arr2[j])
        odd +=2

print("enter the val's into array 1: ")
arr1 = createIntArr()
print("enter the val's into array 2: ")
arr2 = createIntArr()
print("Array 1: ", arr1) 
print("Array 2: ", arr2)

mergealternate(arr1, arr2)
print("Merged Array: ",arr1) 