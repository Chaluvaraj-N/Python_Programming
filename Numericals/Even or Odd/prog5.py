#wap to print first n even numbers

def isevenodd(n):
    return n % 2 == 0
start=1
end=int(input("enter a number:"))
while end>0:
    c=isevenodd(start)
    if c:
        print(start,end=" ")
        end-=1
    start+=1