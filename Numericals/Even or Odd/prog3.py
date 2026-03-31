#wap to print all even numbers present in user defined range

def isevenodd(n):
    return n % 2 == 0
num1 = int(input("enter a number:"))
num2 = int(input("enter another number:"))
if num1 > num2:
    print("invalid i/p")
else:
    print("even number")

for i in range(num1, num2+1):
    flag=isevenodd(i)
    if flag:
        print(i,end=" ")