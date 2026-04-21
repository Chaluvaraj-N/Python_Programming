def createIntArr():
    print("enter the elements for an array to be created: ")
    l1 = []
    while True:
        try:
            n = int(input("enter the num: "))
            l1.append(n)
        except Exception as e:
            return l1
def displaySubArr(arr):
    for i in range(len(arr)):
        res = []
        for j in range(i, len(arr)):
            res.append(arr[j])
            print(res)
arr = createIntArr()
print("the original array is: ", arr)
displaySubArr(arr)

        