# infinite while loop :- a while loop can run infinitely if the condition never becomes false.


n=100
while True:
    print(n)
    n-=1

#break the infinite while loop

while True:
    line = input("Enter a number: ")
    if line == "q":
        break
    print("You entered: ",line)