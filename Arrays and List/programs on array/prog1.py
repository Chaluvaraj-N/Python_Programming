#method of array using try and except Exception

n=input("enter a num:")
print(type(n))
print(n)

print("========================")


#an exception is occured when "_" is imserted

try:
    n=int(input("enter a number:")) #exception
    print(type(n))
    print(n)
except Exception as e:
    print("invalid o/p")