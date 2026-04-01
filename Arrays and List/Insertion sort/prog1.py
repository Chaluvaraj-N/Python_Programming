def insertionsort(arr):
    n=len(arr)
    #cycles
    for i in range(0,n-1):
    #comparison logic with next neighouring value
        for j in range(i+1,0,-1):
            if arr[j-1] > arr[j]:
                arr[j-1],arr[j] = arr[j], arr[j-1]
            else:
                break
    return arr


def createarray():
    print("enter the element into the arr to be created")
    l1=[]
    while True:
        try:
            n=int(input("enter the value:"))
            l1.append(n)
        except Exception as e:
            return l1

arr = createarray()
print("original array:", arr)
insertionsort(arr)
print("sorted array in ascending order:",arr )
    