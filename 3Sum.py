def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        n = len(nums)
        if n<3:
            return []
        
        for i, num in enumerate(nums):
            if i>=1 and nums[i-1] == num:
                continue
            dic = {}
            
            for x in nums[i+1:]:
                if x not in dic:
                    dic[-num-x] = 1
                else:
                    res.add((x, num, -x-num))
                    
        return map(list, res)
