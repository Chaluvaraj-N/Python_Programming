#Te remove a digits from RHS in given num => "n//10"

#to carry forward the current cycles updated value to the next cycle for futher opertions utilize the same varibale on RHS for operation and left or updation   



def countdigits(num):
    count = 0
    while num > 0:
        num = num//10
        count = count+1
    return count
num=int(input("enter the number"))
res = countdigits(num)
print(f"the count digits in {num}: is {res}" )
