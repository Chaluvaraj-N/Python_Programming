#wap to check whether a given 3-digit number is an armstrong number

#an n-digit armstrong number is a special number which is equal to the sum of its own digits, each raised to the power of n

def countarm(num):
    count = 0
    while num > 0:
        num // 10
        count +=1
    return count
n = int(input("enter the number: "))
m = n
p = countarm(n)
asn = 0
while n > 0:
    base = n % 10
    asn = asn + (base ** p)
    n = n // 10
print("the asn given is: ",m)
print("the asn number got is: ", asn)
if asn == m:
    print("same")
else:
    print("different")