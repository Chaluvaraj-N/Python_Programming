# Immediately stops the loop and comes outside the loop

for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("=================================")


#Search number
nums = [10, 20, 30, 40]
for n in nums:
    if n == 30:
        print("Found")
        break




# 📌 Where to use?

# ✔ When you want to exit loop early
# ✔ Searching element
# ✔ Stop condition reached