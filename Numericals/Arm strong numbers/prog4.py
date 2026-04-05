#wap to print all the ASN of a defined range

def countdigits(n):
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
        asn = asn *-1
    return asn == temp
start = int(input("Enter the starting number: "))
end = int(input("Enter the last number: "))
if start > end:
    print("invalid input")
else:
    print("ASN in the given range: ")
    for i in range (start, end + 1):
        if isASN(i):
            print(i, end = " ")

