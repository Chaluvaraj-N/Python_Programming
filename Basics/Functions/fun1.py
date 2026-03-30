#function :- a function is a resuable block of code that performs a specific task. It helps to break down a program into smaller and modular chunks, making it easier to read, maintain, and debug. and it is independent of code that is include to perform a specific task. it can be called multiple times in a program, and it can also take input parameters and return output values.

def greetings():
    print("hello good morning")
greetings()
print("================================")



#funaction with parameters :- parameters are varibales used to pass data into a function 

def love(boy,girl):
    print(f"Boy name is {boy}")
    print(f"Girl name is {girl}")
    print(f"{boy} loves {girl}")

love("chaluva","chaluvii") #positional arguments
print("================================")
love(boy="ujwal",girl="Disha") #keyword arguments
print("================================")



#table creation using function

def tables(num):
    for i in range(1,11):
        print(f"{num} X {i} = {num*i}")
tables(5)



#returning values from function

def add(a,b):
    return a+b
result = add(10,20)
print(f"the sum of 10 and 20 is {result}")

print("================================")

def func(num):
    if num%2==0:
        return "even"
    else:
        return "odd"


#local and global variables


def func():
    x="chaluva"
    print(x) #local variable

    print(y) #global variable
y="ujwal" #global variable
func()
