def createarr():
    li=[]
    print("enter")
    try:
        while True:
            n=int(input("-> "))
            li.append(n)
    except Exception as e:
        return li

createarr()