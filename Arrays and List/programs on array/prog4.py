#print first chr in value in string


def createStrarray():
    print("enter the values into the string to be created: ")
    l1=[]
    while True:
        n=input("enter value: ")
        if n=="":
            return l1
        l1.append(n[:1])
        
str = createStrarray()
print("original Str: ", str)