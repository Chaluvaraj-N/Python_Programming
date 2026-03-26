# # # Used to check multiple conditions

age = int(input("Enter your age: "))

if age >= 60:
    print("Senior citizen")
elif age >= 35:
    print("Adult")
    print("focus on you carrer")
elif age >= 18:
    print("Teen age")
    print("focus on you studies")
elif age >= 10:
    print("Child")
    print("play and enjoy")
else:
    print("baby")
    print("enjoy your childhood")


print("================================================")


a = int(input("enter first number: "))
b = int(input("enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Invalid operator")