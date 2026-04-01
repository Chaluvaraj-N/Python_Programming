# wap to reverse a given interger array

def reversearr(arr):
    i=0
    j=len(arr)-1
    while i<j:
        arr[i],arr[j] = arr[j],arr[i]
        j-=1
        i+=1
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
res=reversearr(arr)
print("reversed array:", res)