#sum of first n natural numbers


n=int(input("Enter a number: "))
sum=0
while n>0:
    sum += n
    n-=1 
print("The sum is: ",sum)