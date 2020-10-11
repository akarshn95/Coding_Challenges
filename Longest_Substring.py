#Given a string s, find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        max_len, start = 0, 0
        
        for i, val in enumerate(s):
            if val in dic:
                # new start is from the index right after the last repeating instance
                new_start = dic[val] + 1
                start = max(new_start, start)
            
            dic[val] = i
            curr_len = i + 1 - start
            max_len = max(max_len, curr_len)
            
        return max_len
