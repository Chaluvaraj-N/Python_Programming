#WAP to print 1 to 8(n) with a incrementing  diff starting from 1

n=int(input("enter the number:"))
i=1
diff=1
while i<=n:
    print(i,end=" ")
    i=i+diff
    diff=diff+1
print("\n last updated i: ",i )