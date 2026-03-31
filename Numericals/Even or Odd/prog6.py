#wap to extract vowels from a string

def extract_vowels(s):
    vowels = "aeiouAEIOU"
    result = ""

    for ch in s:
        if ch in vowels:
            result += ch

    return result


text = input("Enter a string: ")
v = extract_vowels(text)

print("Vowels in the string are:", v)