#peak element

class Solution:   
    def peakElement(self, arr):
    
        n = len(arr)

        #the length of the array is n==1
        if n == 1:
            return 0
        
        #the peak is in b/w
        for i in range(1, n - 1):
             if arr[i - 1] < arr[i] > arr[i + 1]:
                return i
             
        #if the peak is in the last index
        if arr[n - 1] > arr[n - 2]:
            return (n - 1)
        return 0