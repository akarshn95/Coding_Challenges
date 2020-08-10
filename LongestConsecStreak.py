class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_streak = 0
        nums = set(nums)
        
        for num in nums:
            if num-1 not in nums:
                curr_streak=1
                curr_num=num
                
                while curr_num+1 in nums:
                    curr_num+=1
                    curr_streak+=1
                    
                max_streak = max(max_streak, curr_streak)
                
        return max_streak
