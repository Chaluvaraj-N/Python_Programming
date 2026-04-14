# converting lowercase to uppercase

def toUppercase(s):
    nstr = ""
    for i in range(0, len(s)):
        if "a" <= s[i] <= "z":
            nstr = nstr + chr(ord(s[i]) - 32)
        else:
            nstr = nstr + s[i]
    return nstr

s = input("Enter a string: ")
print("original string:", s)

res = toUppercase(s)
print("lower to upper:", res)