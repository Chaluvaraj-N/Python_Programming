# WAP to sum the numbers present in a string and append at the end
# Input: 12ab12c100
# Output: abc124

s = input("Enter the string: ")
print("Original string:", s)

sum = 0
num = ""
res = ""

for i in range(len(s)):
    if '0' <= s[i] <= '9':
        num = num + s[i]
    else:
        if num != "":
            sum = sum + int(num)
            num = ""
        res = res + s[i]

# last number check
if num != "":
    sum = sum + int(num)

print("Result:", res + str(sum))