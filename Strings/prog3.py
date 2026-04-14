# input example: R1At ?tLe

s = input("Enter a string: ")
print("Original string:", s)
print("--------")

# lowercase to uppercase
def toUppercase(s):
    nstr = ""
    for i in range(len(s)):
        if "a" <= s[i] <= "z":
            nstr = nstr + chr(ord(s[i]) - 32)
        else:
            nstr = nstr + s[i]
    return nstr


# uppercase to lowercase
def toLowercase(s):
    nstr = ""
    for i in range(len(s)):
        if "A" <= s[i] <= "Z":
            nstr = nstr + chr(ord(s[i]) + 32)
        else:
            nstr = nstr + s[i]
    return nstr


# swap case
def swapcase(s):
    nstr = ""
    for i in range(len(s)):
        if "a" <= s[i] <= "z":
            nstr = nstr + chr(ord(s[i]) - 32)
        elif "A" <= s[i] <= "Z":
            nstr = nstr + chr(ord(s[i]) + 32)
        else:
            nstr = nstr + s[i]
    return nstr


print("Lower to Upper:", toUppercase(s))
print("--------")
print("Upper to Lower:", toLowercase(s))
print("--------")
print("Swap Case:", swapcase(s))