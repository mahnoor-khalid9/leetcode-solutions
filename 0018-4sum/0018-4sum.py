class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        
        nums.sort()
        n = len(nums)

        quad_list = set()
        for i in range(n-3):
            for j in range(i+1, n-2):
                left = j+1
                right = n-1
                while left < right:

                    current_sum = (
                        nums[i] + nums[j]
                        + nums[left] + nums[right]
                    )


                    if current_sum < target: 
                        left += 1

                    elif current_sum > target:
                        right -= 1
                    
                    elif current_sum == target:
                        quad_list.add((nums[i], nums[j], nums[left], nums[right]))
                        left+=1
                        right-=1

        return [list(quad) for quad in quad_list]
