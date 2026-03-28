#WAP to display the minimum element present in given array along with index

# constraints:

    # 1 <= len(arr) <= 10**4
    # 10**6 <= arr[i] <= 10**6
    # sorting the array is not allowed

def createIntArr():
    print("enter the element into the arr to be created")
    l1=[]
    while True:
        try:
            n=int(input("enter the value:"))
            l1.append(n)
        except Exception as e:
            return l1
        
def findminele(arr):
    minele, mineleind=2**32,-1
    for i in range(0,len(arr)):
        if arr[i] <= minele:
            minele=arr[i]
            mineleind=i
    return minele,mineleind
arr=createIntArr()
print("original arr", arr)
resMin, resMinind=findminele(arr)
print(f"The min ele in the arr is: {resMin} at index:{resMinind}")