class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_area = 0

        while left < right:
            h = min(heights[left], heights[right])
            w = right - left
            area = h * w
            max_area = max(max_area, area)
            if heights[left] > heights[right]:
                right-=1
            else:
                left+=1
        
        return max_area