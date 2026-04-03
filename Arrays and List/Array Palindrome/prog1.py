#wap to check whether the given array is palindrome or not

def intarr():
    l1=[]
    while True:
        try:
            n=int(input("Enter a num:"))
            l1.append(n)
        except:
            return l1
def isArrPallindrome(arr):
    i,j=0,len(arr)-1
    while i<j:
        if arr[i]!=arr[j]:
            return False
        i+=1
        j-=1
    return True
arr=intarr()
print("Original arr:",arr)
flag=isArrPallindrome(arr)
if flag:
    print("Array is pallindrome")
else:
    print("Array is not an pallindrome")