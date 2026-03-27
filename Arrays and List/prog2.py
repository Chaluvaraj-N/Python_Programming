#WAP to create a dynamic integer array

def createIntarray():
    print("enter the elements into the array to be created: ")
    l1=[]
    while True:
        try:
            n=int(input("enter num: "))
            l1.append(n)
        except Exception as e:
            return l1
arr = createIntarray()
print("original arr: ", arr)