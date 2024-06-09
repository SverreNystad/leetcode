class Solution:
    def maxArea(self, height: list[int]) -> int:
        if len(height) <= 1:
            raise ValueError(
                f"Can not have only {len(height)} items in collection height"
            )

        if sum(1 for h in height if h < 0):
            raise ValueError("Can not have negative values in collection height")

        largest_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            # Find the area
            h = min(height[left], height[right])
            w = abs(left - right)
            area = h * w
            if area > largest_area:
                largest_area = area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return largest_area
