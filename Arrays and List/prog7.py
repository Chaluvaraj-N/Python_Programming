#WAP to return positive differene of the product and sum of all element's in a given array

# example :- arr=[10,20,30]
#         product=6000
#         sum=60
#         output:- difference=5940

def intarray():
    l1 = []
    while True:
        try:
            n = int(input("Enter a number: "))
            l1.append(n)
        except:
            return l1

arr = intarray()

def finddiff(arr):
    prod = 1
    total_sum = 0

    for i in range(len(arr)):
        total_sum += arr[i]
        prod *= arr[i]

    diff = prod - total_sum

    if diff < 0:
        diff = -diff

    return total_sum,prod, diff

s,p,d= finddiff(arr)

print("Array:", arr)
print(f"sum is {s}\n prod is {p} \n diff is{d}")
