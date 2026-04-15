#wap to check the given string is a palindrome or not.

#string Palindrome:- A string is said to be a palindrome if and only if it is read same in forword and backword direction, ignoring the spaces, special symbols and casing of the alphabets.

def strFilterations(s):
    nstr = ""
    for i in range(0, len(s)):
        if "A" <= s[i] <= "Z":
            nstr = nstr + chr(ord(s[i]) + 32)
        elif("0" <= s[i] <= "9") or ("a" <= s[i] <= "z"):
            nstr = nstr + s[i]
    return nstr

def isstrpalindrome(s):
    s = strFilterations(s)
    left, right = 0, (len(s) - 1)

    while left < right:
        if s[left]!= s[right]:
            return False
        left +=1
        right -=1
    return True
    
s = input("enter a string")
flag = isstrpalindrome(s)
if flag:
    print("String is palindrome")
else:
    print("string is not palindrome")


