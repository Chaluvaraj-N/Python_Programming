#reversal of string

def reverse_string(s):
    nstr = " "
    for i in range(0, len(s)):
        nstr = s[i] + nstr
    return nstr
s = input("Enter a string: ")
print("The original string is: ", s)
res = reverse_string(s)
print("The reversed string is: ", res)

print("=================using recursion=====================")

def strIncreRevRec(s,nstr,i):
    if i>=len(s):
        return nstr
    nstr=s[i]+nstr
    return strIncreRevRec(s,nstr,(i+1))

s=input("Enter :")
print("Original String:",s)
res=strIncreRevRec(s," ",0)
print("Reverse String using Recursion:",res)

print("=================using increment logic and decrement logic without using recursion=====================")

def strIncreRev(s):
    nstr = " "
    for i in range(0, len(s)):
        nstr = s[i] + nstr
    return nstr
s = input("Enter a string: ")
print("The original string is: ", s)
res = strIncreRev(s)
print("The reversed string is: ", res)


