#wap to merge the given 2 integer arrays at alternate indices 

def createIntArr():
    l1=[]
    while True:
        try:
            n = int(input("enter valu: "))
            l1.append(n)
        except Exception as e:
            return l1
def mergeAlternative(arr1, arr2):
    res = [] #creation of 3rd memory
    n1, n2 = len(arr1), len(arr2)
    i,j=0,0
    #the imaginary cursor on res
    for k in range(0,(n1+n2)):
        if i < n1 and k % 2 == 0:
            res.append(arr1[i])
            i += 1
        elif j < n2 and k % 2 == 0:
            res.append(arr2[j])
            j += 1
        else: #special case
            if i < n1: #extra val's are in arr1
                res.append(arr2[i])
                i += 1
            elif j < n2: #extra val's are in arr2
                res.append(arr2[j])
                j += 1
            else: #special case
                if i<n1: #extra values are in arr1
                    res.append(arr1[i])
                    i+=1
                elif j<n2:
                    res.append(arr2[j])
                    j+=1
    return res

print("enter the val's into array 1: ")
arr1 = createIntArr()
print("enter the val's into array 2: ")
arr2 = createIntArr()
print("Array 1: ", arr1) 
print("Array 2: ", arr2)
res = mergeAlternative(arr1, arr2)
print("Merged Array: ", res) 