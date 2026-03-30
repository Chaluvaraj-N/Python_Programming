# | Statement | Works in | Action         |
# | --------- | -------- | -------------- |
# | break     | loop     | exit loop      |
# | continue  | loop     | skip iteration |
# | return    | function | exit function  |


# 🔥 EASY MEMORY TRICK
# break → STOP loop
# continue → SKIP step
# return → GO BACK with value


for i in range(1, 10):
    if i == 3:
        continue
    if i == 7:
        break
    print(i)


# REAL LIFE UNDERSTANDING
# break → Stop exam when bell rings 🔔
# continue → Skip one question
# return → Submit paper and exit