#kth missing positvi number using for loop

class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:

        for i in range(0, len(arr)):
            if arr[i] <= k:
                k += 1
            else:
                break
        return k
