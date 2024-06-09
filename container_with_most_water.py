class Solution:
    def maxArea(self, height: list[int]) -> int:
        if len(height) <= 1:
            raise ValueError(
                f"Can not have only {len(height)} items in collection height"
            )

        if sum(1 for h in height if h < 0):
            raise ValueError("Can not have negative values in collection height")

        largest_area = 0
        i = 0
        j = len(height) - 1
        while i != j:
            c1 = height[i]
            c2 = height[j]

            # Find the area
            h = c1 if c1 < c2 else c2
            w = abs(i - j)
            area = h * w
            if area > largest_area:
                print(f"c1: {c1}, c2: {c2}")
                largest_area = area

            if c1 < c2:
                i += 1
            else:
                j -= 1
        return largest_area
