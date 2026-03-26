arr=[]
print(len(arr))

# print(arr[0])

arr.append(10)
arr.append("abc")
arr.append(23.6)
print(len(arr))
print(arr[len(arr)-1])
arr.append(100)
print(arr)
arr[3]=25

arr.insert(1,45)
print(arr)
arr.insert(20,200)
print(arr)
l2=[1,2,3]
l3=[55,65]
l2.append(l3)
print(l2)
print(l3)
l2[3][1]
print(l2)
print(l3)
l4=[5,6]
l5=[100,200,300]
print(l4)
print(l5)
l4.extend(l5)
print(l4)
print(l5)
l5[2]=65
print(l4)
print(l5)

# l4.extend(25) #error (because we cannot pass single valued data)