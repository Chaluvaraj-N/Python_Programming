# 1. o/p is in boolen value
# 2. i/p is in constants, expression, boolen value/condition
# 3. it holds pre-defined value (true=1, flase=0, none=ntg)
# 4. the initial letter is upper case


# Variables for comparison
a = 10
b = 5
c = 10

# Equal to (==)
print(f"a == c: {a == c}")  # True
print(f"a == b: {a == b}")  # False

# Not equal to (!=)
print(f"a != b: {a != b}")  # True
print(f"a != c: {a != c}")  # False

# Greater than (>)
print(f"a > b: {a > b}")    # True
print(f"b > a: {b > a}")    # False

# Less than (<)
print(f"b < a: {b < a}")    # True
print(f"a < b: {a < b}")    # False

# Greater than or equal to (>=)
print(f"a >= c: {a >= c}")  # True
print(f"a >= b: {a >= b}")  # True

# Less than or equal to (<=)
print(f"b <= a: {b <= a}")  # True
print(f"a <= b: {a <= b}")  # False

# Chaining comparisons
print(f"b < a < 15: {b < a < 15}")  # True (a is between b and 15)

print((33 ** True) >= (33 ** False))