#wap to print first "n" ASN

def countdigits(n):
    if n == 0:      
        return 1
    count = 0
    while n > 0:
        n = n // 10
        count = count + 1
    return count   

def isASN(num):
    temp = num

    if num < 0:
        num = num * -1

    pow = countdigits(num)   
    asn = 0                 

    while num > 0:
        base = num % 10      
        asn = asn + (base ** pow)
        num = num // 10      

    if temp < 0:
        asn = asn * -1

    return asn == temp


n = int(input("Enter how many ASN values you want: "))
count = 0
num = 1

print(f"First ASN values are {n}: ") 

while count < n:
    if isASN(num):
        print(num, end=" ")
        count += 1
    num += 1