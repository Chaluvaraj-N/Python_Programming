#wap to reverse the position of the words wihout reversing the each individual word

def reversalword(s):
    s = s + " "
    nwrd, nsen = "", ""
    for i in range(0, len(s)):
        if s[i]!= " ":
            nwrd += s[i]
        elif nwrd != "":
            if nsen == "":
                nsen = nwrd + nsen
            else:
                nsen = nwrd + " " + nsen
            nwrd = ""
    return nsen
   
s = input("Enter a string")
print("original String: ", s)
res = reversalword(s)
print("String with reversed word:", res)
    