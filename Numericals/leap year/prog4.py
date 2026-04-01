#print leap and non leap year separately in a given range

def is_leap_year(year):
    return (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0)
sr = int(input("enter the starting range:"))
er = int(input("enter the ending range:"))
if sr > er:
    print("invalid i/p")
else:
    print("leap year")
    for i in range(sr, er + 1):
        flag = is_leap_year(i)
        if flag:
            print(i,end=" ")
    print("\nnon leap year")
    for i in range(sr, er + 1):
        flag = is_leap_year(i)
        if not flag:
            print(i,end=" ")
        