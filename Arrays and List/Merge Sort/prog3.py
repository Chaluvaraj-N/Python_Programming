#wap to merge the given 2 asc sorted array in asc order

def createIntArr():
    l1=[]
    while True:
        try:
            n = int(input("enter valu: "))
            l1.append(n)
        except:
            return l1
        
def mergeAscSorted(arr1, arr2):
    res=[]
    n1, n2 = len(arr1), len(arr2)
    i, j = 0, 0

    for k in range(0, (n1 + n2)):
        if i < n1 and j < n2:
            if arr1[i] <= arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])  
                
                j += 1
        else:
            if i < n1:
                res.append(arr1[i])
                i += 1
            elif j < n2:
                res.append(arr2[j])
                j += 1

    return res


print("enter the val's into array 1: ")
arr1 = createIntArr()

print("enter the val's into array 2: ")
arr2 = createIntArr()

print("Array 1: ", arr1) 
print("Array 2: ", arr2)

print(mergeAscSorted(arr1, arr2))