#it will help to find positivi and negative integer in ASN 

def countdigits(n):
    count = 0
    while n > 0:
        n = n // 10
        count = count + 1
    return count

n = int(input("enter num: "))
temp = n

if n < 0:
    n = n * -1

pow = countdigits(n)
asn = 0

while n > 0:
    base = n % 10
    asn = asn + (base ** pow)
    n = n // 10

if temp < 0:
    asn = asn * -1

if asn == temp:
    print(f"{temp} is an ASN")
else:
    print(f"{temp} is not an ASN")
