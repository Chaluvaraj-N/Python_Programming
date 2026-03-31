#wap to print the 2nd largest element in a given array along with its index


def createintarr():
    a1=[]
    print("enter the elements into the array to be created:")
    while True:
        try:
            n=int(input("enter the number of elements in the array:"))
            a1.append(n)
        except Exception as e:
            return a1
def findsecmax(arr):
    maxele,exeleind= -2**31,-1
    secmaxele,secmaxeleind=-2**31,-1
    for i in range(0,len(arr)):
        if maxele<arr[i]:
            secmaxele,secmaxeleind=maxele,exeleind
            maxele,exeleind=arr[i],i
        elif maxele != arr[i] and secmaxele < arr[i]:
            secmaxele,secmaxeleind=arr[i],i
    return [maxele,exeleind,secmaxele,secmaxeleind]
arr=createintarr()
print("original array:",arr)
res=findsecmax(arr)
print("max element:",res[0],"index of max element:",res[1])
print("2nd max element:",res[2],"index of 2nd max element:",res[3])