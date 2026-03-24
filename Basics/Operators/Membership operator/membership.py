# [in, not in ]

# it can only be used on iterablr objects on group of elements

# it check whether this specified element is available within the group of elements  

s1="alpha12"
print("a" in s1)
print("A" in s1)
print("hla" in s1)
print("12" is s1)
print("a12" in s1)

x=100
print("1" in x)    # TypeError: argument of type 'int' is not iterable

x="100"
print("1" in x)    # True, because "1" is a substring of "