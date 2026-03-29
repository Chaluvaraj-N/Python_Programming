#while loop with else statement :- when the while conditon becomes false, the else block is executed.

fruits=["apple","banan","mongo","grapes"]
fruits_len=len(fruits)
index=0

while index < fruits_len:
    if fruits[index]=="orange":
        print("orange is found at index: ",index)
        break
    index+=1
else:
    print("orange is not found in the list")