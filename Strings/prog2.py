# converting uppercase to lowercase

def toLowercase(s):
    nstr = ""
    for i in range(0, len(s)):
        if "A" <= s[i] <= "Z":
            nstr = nstr + chr(ord(s[i]) + 32)
        else:
            nstr = nstr + s[i]
    return nstr

s = input("Enter a string: ")
print("original string:", s)

res = toLowercase(s)
print("upper to lower:", res)