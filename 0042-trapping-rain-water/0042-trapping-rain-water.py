class Solution:
    def trap(self, height: list[int]) -> int:
        left_max = [0] * len(height)
        right_max = [0] * len(height)

        for i in range(len(height)):
            left_max[i] = max(
                height[i],
                left_max[i - 1] if i > 0 else 0
            )

        for i in range(len(height) - 1, -1, -1):
            right_max[i] = max(
                height[i],
                right_max[i + 1] if i < len(height) - 1 else 0
            )
        
        area = 0
        for i in range(len(height)):
            area += min(left_max[i], right_max[i]) - height[i]


        print(left_max, right_max)

        return area
                