#WAp to rotate an array 

# there are 2 varities of rotation 
#     1.Left
#     2.right


#left rotation 

def reversalarray(arr,i,j):
    while i < j:
        arr[i],arr[j]=arr[j],arr[i]
        i += 1
        j -= 1
def leftrotation(arr,k):
    n = len(arr)
    if k >= n:
        k = k%n
    reversalarray(arr,0,(k-1))
    reversalarray(arr, k, (n-1))
    reversalarray(arr,0,(n-1))

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
k=int(input("Enter a num:"))
print("original array:", arr)
leftrotation(arr,k)
print("leftrotation:", arr)