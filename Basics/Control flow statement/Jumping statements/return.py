# Used inside function to: return value and stop function execution


#return sum
def add(a, b):
    return a + b

print(add(2, 3))

print("=================================")

# Stop function early

def check(num):
    if num < 0:
        return "Negative"
    return "Positive"

print(check(-5))



# 📌 Where to use?

# ✔ Functions
# ✔ Calculations
# ✔ Returning result