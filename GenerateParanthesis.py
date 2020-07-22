# Given a number generate all closed combinations of 2*n paranthesis

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        
        def backtrack(S='',left=0,right=0):
            if len(S)==2*n:
                res.append(S)
                return
            # add left and right paranthesis only if it is 'allowed' by checking the number of left and right paranthesis
            if left<n:
                backtrack(S+'(',left+1,right)
            if right<left:
                backtrack(S+')',left,right+1)
        backtrack()      
        return res
