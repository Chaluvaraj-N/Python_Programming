#wap to print all leap year available in the given range

def is_leap_year(year):
    if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
        return True
    else:
        return False
sr = int(input("enter the starting range:"))
er = int(input("enter the ending range:"))
if sr > er:
    print("invalid i/p")
else:
    print("leap years:")
    for i in range(sr, er + 1):
        flag = is_leap_year(i)
        if flag:
            print(i,end=" ")