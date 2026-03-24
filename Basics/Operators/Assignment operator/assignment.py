# var_name = value
number = 10
print(number) #storage location = value



#var_name = initialized_var_name + value
number = number + 5
print(number) #copy value from storage location and add 5 to it and store the result in the same storage location



# assignment operator + arithmetic operator
x = 10

x += 5    # 10 + 5 = 15
x -= 3    # 15 - 3 = 12
x *= 2    # 12 * 2 = 24
x /= 4    # 24 / 4 = 6.0
x %= 5    # 6 % 5 = 1.0
x //= 1   # 1.0 // 1 = 1.0
x **= 3   # 1.0 ** 3 = 1.0

print(x)  


# assignment operator + bitwise operator
x = 5   # 101
y = 3   # 011

x &= y   # 101 & 011 = 001 → 1
x |= y   # 001 | 011 = 011 → 3
x ^= y   # 011 ^ 011 = 000 → 0
x <<= 2  # 000 << 2 = 0000 → 0
x >>= 1  # 0000 >> 1 = 000 → 0

print(x)  


#in python, we can also use assignment operator with strings
greeting = "Hello"
greeting += ", World!"  
print(greeting)  

#note in assignment operator ~= is not a valid operator in python, it is used in some other programming languages for approximate equality comparison. In python, we can use math.isclose() function for that purpose.

#note in python, we can also use assignment operator with lists
numbers = [1, 2, 3]
numbers += [4, 5]
print(numbers)