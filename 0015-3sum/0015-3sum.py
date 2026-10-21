class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        def min_heapify(nums, i, n):
            smallest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and nums[left] < nums[smallest]:
                smallest = left

            if right < n and nums[right] < nums[smallest]:
                smallest = right

            if smallest != i:
                nums[i], nums[smallest] = nums[smallest], nums[i]
                min_heapify(nums, smallest, n)

        # Stage 1: Build min-heap
        n = len(nums)

        for i in range(n // 2 - 1, -1, -1):
            min_heapify(nums, i, n)

        # Stage 2: Extract elements in sorted order
        sorted_nums = []

        while nums:
            sorted_nums.append(nums[0])
            last_element = nums.pop()

            if nums:
                nums[0] = last_element
                min_heapify(nums, 0, len(nums))

        # Stage 3: Find unique triplets
        result = []

        for i in range(len(sorted_nums) - 2):

            # Skip duplicate fixed elements
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            left = i + 1
            right = len(sorted_nums) - 1

            while left < right:
                current_sum = (
                    sorted_nums[i]
                    + sorted_nums[left]
                    + sorted_nums[right]
                )

                if current_sum == 0:
                    result.append([
                        sorted_nums[i],
                        sorted_nums[left],
                        sorted_nums[right]
                    ])

                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                        left += 1

                    # Skip duplicate right values
                    while left < right and sorted_nums[right] == sorted_nums[right + 1]:
                        right -= 1

                elif current_sum < 0:
                    left += 1

                else:
                    right -= 1

        return result