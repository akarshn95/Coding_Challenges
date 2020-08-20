class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # dummy bar to stop all counting areas at the end
        heights.append(0)
        stack = [-1]
        res = 0
        for i in range(len(heights)):
            # stop the current rectangle if height dips
            while heights[i]<heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] -1
                res = max(res, height*width)
            stack.append (i)
        return res
