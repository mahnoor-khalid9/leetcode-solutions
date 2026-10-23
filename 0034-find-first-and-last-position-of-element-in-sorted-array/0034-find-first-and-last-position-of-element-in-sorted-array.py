class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        l = 0
        r = len(nums)-1
        index = [-1, -1]

        while l<=r:
            m = l + (r-l) // 2
            if target < nums[m]:
                r = m-1
            elif target > nums[m]:
                l = m+1
            
            else:
                target = nums[m]
                index[0] = m
                r = m-1
        
        # Reset pointers for second binary search
        l = 0
        r = len(nums) - 1

        while l<=r:
            m = l + (r-l) // 2
            if target < nums[m]:
                r = m-1
            elif target > nums[m]:
                l = m+1
            
            else:
                target = nums[m]
                index[-1] = m
                l = m+1
        
        return index
            




        