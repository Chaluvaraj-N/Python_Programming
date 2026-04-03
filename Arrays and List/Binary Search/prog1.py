#ascending


def Intarr():
    l1=[]
    while True:
        try:
            n=int(input("Enter a num:"))
            l1.append(n)
        except:
            return l1
def binarysearchasc(arr,target):
    start,end=0,len(arr)-1
    while start<=end:
        mid=(start+end)//2
        if target==arr[mid]:
            return mid
        if target<arr[mid]:
            end=mid-1
        else:
            start=mid+1
    return -1
arr=Intarr()
target=int(input("Enter an element to br searched:"))
print("Original array:",arr)
index=binarysearchasc(arr,target)
if index==-1:
    print("The  not found element found")
else:
    print("The element  found")