#WAP to create a dynamic string array


def createStrarray():
    print("enter the values into the string to be created: ")
    l1=[]
    while True:
        n=input("enter value: ")
        if n=="":
            return l1
        l1.append(n)
        
str = createStrarray()
print("original Str: ", str)