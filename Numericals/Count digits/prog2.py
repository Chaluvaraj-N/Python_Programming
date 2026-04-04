# counting digits, letters and special characters

s = input("enter the string: ")
d=0
l=0
o=0
for i in s:
    if i.isdigit():
        d+=1
    elif i.isalpha():
        l+=1
    else:
        o+=1

print(f"Digits count are: {d}")
print(f"letters counts are: {l}")
print(f"Special characters counts are: {o}")