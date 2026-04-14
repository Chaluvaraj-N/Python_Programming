#wap to sum  the numbers present in a given and join it at end of rest of characters in the string

def sumStrNumber(s):
    nstr,charDig,sumNum='',0,0

    for i in range(0,len(s)):
        if"0" <=s[i]<="9":
            charDig=(charDig*10)+(ord(s[i])-48)

        else:
            if charDig!=0:
                sumNum=sumNum+charDig
                charDig=0
            nstr=nstr+s[i]

    if charDig!=0:
        sumNum=sumNum+charDig
        charDig=0

    return (nstr+str(sumNum))
s=input("Enter a string:")
sumNum=sumStrNumber(s)
print(sumNum)