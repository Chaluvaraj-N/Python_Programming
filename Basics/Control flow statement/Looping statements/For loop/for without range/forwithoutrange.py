#for without range is Used to loop through data directly

# Example (List)

nums = [10, 20, 30]
for i in nums:
    print(i)

#Example (String)

name = "ABC"
for ch in name:
    print(ch)

#example 

for i in [10,20,30]:
    print(i,end=" ")
print("\n=====")
for i in [40,50,60]:
    print(i,end=" ")


# 🔍 How it works
# Takes each value one by one
# No need of index


# 📌 When to use
# ✔ Working with:
# lists
# strings
# tuples
# ✔ When you want values directly

# | for with range | for without range |
# | -------------- | ----------------- |
# | Numbers        | Values            |
# | Uses index     | Uses actual data  |
