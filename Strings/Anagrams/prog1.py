#wap to check wheather the given two string are anagrams are not

#given two strings are set to be anagrams if an only if both the strings consist of the same alphabets
#along with their same number of occurances ignoring the casing, special ymbols, char digits and spaces

def strFilteration(s):
    nstr = ""
    for i in range(0, len(s)):
        if "A" <= s[i] <= "Z":
            nstr+=chr(ord(s[i]) + 32)
        elif "a" <= s[i] <= "z":
            nstr+=s[i]
    return nstr
def anagrams(s1, s2):
    s1 = strFilteration(s1)
    s2 = strFilteration(s2)
    if len(s1) != len(s2):
        return False
    else:
        dict1 = {}
        for i in range(0, len(s1)):
            if s1[i] in dict1:
                dict1[s1[i]]+=1
            else:
                dict1[s1[i]]=1
            if s2[i] in dict1:
                dict1[s2[i]]-=1
            else:
                dict1[s2[i]]=-1
        for key,value in dict1.items():
            if value != 0:
                return False
        return True
s1=input("Enter the first string: ")
s2=input("Enter the second string: ")
flag=anagrams(s1, s2)
if flag:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")