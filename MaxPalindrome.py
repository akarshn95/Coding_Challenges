class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # map the char count to a dictionary
        dic = {}
        for char in s:
            dic[char] = dic.get(char,0)+1
         
        # if it is the first odd number it can still contribute to 1 by being in the middle
        firstOdd = True
        res = 0
        for key in dic:
            res += dic[key]
            # if it is found to be odd, subtract
            if dic[key]%2!=0:
                # if it is the first odd number, let it be
                if firstOdd:
                    firstOdd=False
                    continue
                # if not remove from count
                res -= 1
        return res
