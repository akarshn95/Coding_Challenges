class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            #return # backtracking
        
        # remove one element from the list at each iteration and store it to the path, when all elements are removed, append the path to results
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
            
## https://www.youtube.com/watch?v=KukNnoN-SoY - FOR VISUALIZATION    
