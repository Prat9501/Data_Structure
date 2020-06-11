class Solution:
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        max_height = 0
        while i < j:
            if height[i] < height[j]:
                max_height = max(max_height, height[i] * (j-i))
                i += 1
            else:
                max_height = max(max_height, height[j] * (j-i))
                j -= 1
        return max_height