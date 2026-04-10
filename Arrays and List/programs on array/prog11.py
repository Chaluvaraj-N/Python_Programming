#kth missing positvi number using while loop

class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        
        i = 0
        while i < len(arr) and arr[i] <=k:
            k+=1
            i+=1
        return k
