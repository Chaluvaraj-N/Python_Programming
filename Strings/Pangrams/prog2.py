#wap to return the missing characters in a string their should be include in a given string to make it a program

#constraints :- s[i]=> consists of only lower case alphabet

def missingPangramicAlpa(s):
    ascii = [0]*26
    res = ""

    for i in range(0, len(s)):
        ascii[ord(s[i]) - 97] = ascii[ord(s[i]) - 97] + 1
        #ascii[0] = ascii[0] + 1 ==> 'a'

    #print(ascii)
    for i in range(0, len(ascii)):
        if ascii[i] == 0:
            res = res + chr(i + 97)
    return res

s = "abbbccddeerrffytuwsqtracsg"
res = missingPangramicAlpa(s)
print(res)
