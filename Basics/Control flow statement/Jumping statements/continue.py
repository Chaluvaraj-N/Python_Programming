# Skips current iteration and moves to next

for i in range(1, 10):
    if i == 5:
        continue
    print(i)

print("=================================")


# Print only even numbers

for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)


# 📌 Where to use?

# ✔ Skip unwanted values
# ✔ Filtering data
# ✔ Ignore specific condition