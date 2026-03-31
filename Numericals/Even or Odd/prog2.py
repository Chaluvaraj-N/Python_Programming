#wap to check whether a number is even or odd using customized function

def isevenodd(n):
    if n % 2 == 0:
        return True
    else:
        return False
num = int(input("enter a number:"))
flag = isevenodd(num)
if flag:
    print(f"{num} is even") 
else:
    print(f"{num} is odd")