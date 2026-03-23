# Logical Operators: and, or, not
# it helps to combine and check multiple boolean condition 

# i/p = boolean condition
# o/p = boolean value or anything that represents boolean ValueError

# any number other then 0 is considered to be True



# 1. AND operator - returns True if both conditions are True
x = 10
y = 20
print(x > 5 and y > 15)  # True
print(x > 15 and y > 15)  # False

# 2. OR operator - returns True if at least one condition is True
print(x > 15 or y > 15)  # True
print(x > 15 or y > 30)  # False

# 3. NOT operator - reverses the result
print(not (x > 15))  # True
print(not (x > 5))   # False

# Practical examples
age = 25
has_license = True

# AND: Both conditions must be true
if age >= 18 and has_license:
    print("You can drive")

# OR: At least one condition must be true
is_weekend = True
is_holiday = False
if is_weekend or is_holiday:
    print("No work today!")

# NOT: Inverts the condition
if not is_holiday:
    print("It's a working day")