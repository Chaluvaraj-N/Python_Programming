#Example 1: Print 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1

print("==============")

# Example 2: Print Even Numbers
i = 2
while i <= 10:
    print(i)
    i += 2

print("==============")

# Example 3: Calculate the sum of first 5 natural numbers
i = 1
total = 0
while i <= 5:
    total += i
    i += 1
print("Sum:", total)

print("==============")

# Example 4: Password Validation
password = ""
while password != "1234":
    password = input("Enter password: ")
print("Access granted")

print("==============")

# Example 5: Multiplication Table of 3
i = 1
num = 3
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1