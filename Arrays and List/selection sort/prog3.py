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
def findsecmin(arr):
    minele,exeleind= 2**31,-1
    secminele,secmineleind=2**31,-1
    for i in range(0,len(arr)):
        if minele>arr[i]:
            secminele,secmineleind=minele,exeleind
            minele,exeleind=arr[i],i
        elif minele != arr[i] and secminele > arr[i]:
            secminele,secmineleind=arr[i],i
    return [minele,exeleind,secminele,secmineleind]
arr=createintarr()
print("original array:",arr)
res=findsecmin(arr)
print("min element:",res[0],"index of min element:",res[1])
print("2nd min element:",res[2],"index of 2nd min element:",res[3])