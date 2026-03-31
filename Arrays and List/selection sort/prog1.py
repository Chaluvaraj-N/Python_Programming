def selectionsort(arr):
    n=len(arr)
    #cycles
    for i in range(0,(n-1)):
        actualind=((n-1)-i)
        #current cycles max elements index
        currentMaxEle, currentMaxEleInd=-2**32,-1
        for j in range(0,(actualind + 1)):
            if arr[j] > currentMaxEle:
                currentMaxEle=arr[j]
                currentMaxEleInd=j
        arr[actualind],arr[currentMaxEleInd]=(arr[currentMaxEleInd],arr[actualind])
def createIntArr():
    print("enter the element into the arr to be created")
    l1=[]
    while True:
        try:
            n=int(input("enter the value:"))
            l1.append(n)
        except Exception as e:
            return l1
arr=createIntArr()
selectionsort(arr)
print(arr)
  

print("=========OR[easy method]===========")


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
arr=createIntArr()
print(selection_sort(arr))