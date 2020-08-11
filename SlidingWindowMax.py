class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # first window max
        m = max(nums[:k])
        res = [m]
        
        for i in range(k,len(nums)):
            # compare new element to current max
            m = max(nums[i],m)
            # check if the current m is out of the window 
            if (nums[i-k]==m):
                m = max(nums[i-k+1:i+1])
            res.append(m)
                
        return res
