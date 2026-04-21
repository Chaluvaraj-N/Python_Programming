#displaying of sub arrays


def createIntArr():
    print("enter the elements for an array to be created: ")
    l1 = []
    while True:
        try:
            n = int(input("enter the num: "))
            l1.append(n)
        except Exception as e:
            return l1
def createsubarray(arr):
    res = []
    #start point of sub array @ each cycle
    for i in range(0, len(arr)):
        #end point of sub array formed
        for j in range(i, len(arr)):
            sub = []
            #to insert elements into the sub array
            for k in range(i, j+1):
                sub.append(arr[k])
            res.append(sub)
    return res
arr = createIntArr()
print("the original array is: ", arr)
print("the sub arrays are: ", createsubarray(arr))