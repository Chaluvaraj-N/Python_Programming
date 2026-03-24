# [is, is not]

# The identity operators are used to compare the memory locations of two objects. They check whether two variables point to the same object in memory.

# Output= boolean value (True or False)

a = 10
b = 5 + 5
c = 2 * 5
print(id(a) == id(b) == id(c))    # True, because a and b point to the same memory location
print(a is b is c)    # True, because a b and c point to the same memory location


a="abc"
b="abc"
print(a is b)    # True, because a and b point to the same memory location (string literals are interned in Python)


b="ABC"
print(a is b)    # False, because a and b point to different memory locations (different string literals)

print(not(a is c))    # True, because a and c point to different memory locations (different string literals)

print(a==b==c)    # False, because a, b and c have different values (different string literals) 

print(id(5) is id(2+3))    # False, because id(5) and id(2+3) are different memory locations (id() returns a unique identifier for an object, not the object itself)