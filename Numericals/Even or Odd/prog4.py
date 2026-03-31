#wap to print even and odd numbers separately present in user defined range

def isevenodd(n):
    if n % 2 == 0:
        return True
    else:
        return False

num1 = int(input("enter a number: "))
num2 = int(input("enter another number: "))

if num1 > num2:
    print("invalid input")
else:
    print("even numbers:")
    for i in range(num1, num2 + 1):
        flag = isevenodd(i)
        if flag:
            print(i, end=" ")

    print("\nodd numbers:")
    for i in range(num1, num2 + 1):
        flag = isevenodd(i)
        if not flag:
            print(i, end=" ")