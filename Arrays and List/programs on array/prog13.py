#Palindrome Array

# Your task is to complete this function
# Function should return true/false
def isPalinArray(arr):
    # Code here
    
    n = len(arr)
    for i in range(n):
        s = str(arr[i])
        if s != s[::-1]:
            return False
    return True
