## 1. WAP to segregate btw the duplicate ,non-duplicate present in a array

def createarray():
    print("enter the element into the arr to be created")
    l1=[]
    while True:
        try:
            n=int(input("enter the value:"))
            l1.append(n)
        except Exception as e:
            return l1

def SegregateIt(arr):
    dup,nondup,unique=[],[],[]
    dict={}
    for i in range(0,len(arr)):
        if arr[i] in dict:
            dict[arr[i]]+=1
        else:
            dict[arr[i]]=1
    for key,val in dict.items():
        if val>1:
            dup.append(key)
        if val>=1:
            nondup.append(key)
        if val==1:
            unique.append(key)
    print(f"ORIGINAL ARRAY IS {arr}")
    print(f"The duplicate elemet is {dup}")
    print(f"The NON duplicate elemet is {nondup}")
    print(f"The unique elemet is {unique}")
arr=createarray()
SegregateIt(arr)