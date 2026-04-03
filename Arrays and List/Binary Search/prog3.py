#finding the target element based on sorted arr(asc and desc)

def Intarr():
    l1=[]
    while True:
        try:
            n=int(input("Enter a num:"))
            l1.append(n)
        except:
            return l1
def orderAgnosticBinarysearch(arr,target):
    start,end=0,len(arr)-1
    flag="asc"
    if arr[start]>arr[end]:
        flag="desc"
    while start<=end:
        mid=(start+end)//2
        if target==arr[mid]:
            return mid
        if flag=="asc":
            if target<arr[mid]:
                end=mid-1
            else:
                start=mid+1
        if flag=="desc":
            if target>arr[mid]:
                end=mid-1
            else:
                start=mid+1
    return -1
arr=Intarr()
target=int(input("Enter an element to br searched:"))
print("Original array:",arr)
index=orderAgnosticBinarysearch(arr,target)
if index==-1:
    print("The element not  found")
else:
    print("The element  found")