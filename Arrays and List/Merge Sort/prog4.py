def createIntArr():
    l1=[]
    while True:
        try:
            n = int(input("enter valu: "))
            l1.append(n)
        except:
            return l1
def mergeSortMerging(arr,start,mid,end):
    i,j=start,(mid+1)
    res=[]
    for k in range(0,(mid+end)+1):
        if i <=mid and j <=end:
            if arr[i]<=arr[j]:
                res.append(arr[i])
                i+=1
            else:
                res.append(arr[j])
                j+=1
        else:# extra val's
            if i<=mid:
                res.append(arr[i])
                i+=1
            elif j<=end:
                res.append(arr[j])
                j+=1
    #Update the original memory from res[]
    for k in range(0,len(res)):
        arr[start]=res[k]
        start+=1

def mergesortDivision(arr,start,end):
    if start>=end:
        return
    mid=(start+end)//2
    #LHS division
    mergesortDivision(arr,start,mid)
    #RHS division
    mergesortDivision(arr,mid+1,end)
    #start merging----After base cond the merging works
    mergeSortMerging(arr,start,mid,end)

arr = list(map(int, input("Enter the elements to create the array: ").split()))
print("Original Array:", arr)
mergesortDivision(arr,0,len(arr)-1)
print("Sorted Array:", arr)