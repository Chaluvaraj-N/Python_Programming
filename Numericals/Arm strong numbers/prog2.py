#wap to check whether a given 3-digit number is an armstrong number

num = int(input("enter a 3-digit number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print(f"{num} is an ASN. ")
else:
    print(f"{num} is not an ASN. ")