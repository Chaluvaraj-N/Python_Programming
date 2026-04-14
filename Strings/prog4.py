# WAP to sum all digit characters in a string and append at the end
# Input:  a1P23c4
# Output: aPc10

def sumCharacterDigits(s):
    res = ""
    sumCharDig = 0

    # separate digits and characters
    for i in range(len(s)):
        if "0" <= s[i] <= "9":
            sumCharDig = sumCharDig + (ord(s[i]) - 48)
        else:
            res = res + s[i]

    # -------- LOGIC 1 (manual conversion: int → string) --------
    # num = ""
    # while sumCharDig > 0:
    #     rem = sumCharDig % 10
    #     num = chr(rem + 48) + num
    #     sumCharDig = sumCharDig // 10
    # return res + num


    # -------- LOGIC 2 (easy method using str) --------
    num = str(sumCharDig)
    return res + num


s = input("Enter the string: ")
print("The original string is:", s)

res = sumCharacterDigits(s)
print("The summed string is:", res)