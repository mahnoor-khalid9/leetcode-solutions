class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = dict()
        for index in range(len(nums)):
            comp = target - nums[index]

            if comp in seen.keys():
                return [index, seen[comp]]
            seen[nums[index]] = index
