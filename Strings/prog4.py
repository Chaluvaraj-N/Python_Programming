# WAP to sum all digit characters in a string and append at the end
# Input:  a1P23c4
# Output: aPc10

def sumCharacterDigits(s):
    res = ""
    sumCharDig = 0

    for i in range(len(s)):
        if "0" <= s[i] <= "9":
            sumCharDig = sumCharDig + (ord(s[i]) - 48)
        else:
            res = res + s[i]

    num = str(sumCharDig)
    return res + num


s = input("Enter the string: ")
print("The original string is:", s)

res = sumCharacterDigits(s)
print("The summed string is:", res)