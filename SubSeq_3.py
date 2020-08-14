# Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        
        for num in nums:
            if num<=first:
                first=num
            elif num<=second:
                second=num
            else:
                return True
        return False
