#wap to reverse the each indiviudal word of given string without reversing the positing words ("Word reversal")

def reversalword(s):
    s = s + " "
    nwrd, nsen = "", ""
    for i in range(0, len(s)):
        if s[i]!= " ":
            nwrd = s[i] + nwrd
        elif nwrd != "":
            if nsen == "":
                nsen = nsen + nwrd
            else:
                nsen = nsen + " " + nwrd
            nwrd = ""
    return nsen
   
s = input("Enter a string")
print("original String: ", s)
res = reversalword(s)
print("String with reversed word:", res)
    

