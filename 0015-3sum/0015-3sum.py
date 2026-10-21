class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        def min_heapify(nums, i, n):
            smallest = i
            left_node = 2*i+1
            right_node = 2*i+2
            if left_node < n and nums[i] > nums[left_node]:
                smallest = left_node
            if right_node< n and nums[smallest] > nums[right_node]:
                smallest = right_node
            if smallest != i:
                nums[i], nums[smallest] = nums[smallest], nums[i]
                min_heapify(nums, smallest, n)


        n = len(nums)
        for i in range ((n-1)//2, -1, -1):
            min_heapify(nums, i, n)

        sn = list()
        for i in range(n-1, -1, -1):
            sn.append(nums[0])
            last_element = nums.pop()
            
            if nums:
                nums[0] = last_element
                n = len(nums)
                min_heapify(nums, 0, n)



        list_ = set()
        for i in range(len(sn)):
            l = i+1
            r = len(sn)-1
            while l<r:
                if sn[i] + sn[l] + sn[r] == 0:
                    list_.add((sn[i], sn[l], sn[r]))
                    l+=1
                    r-=1

                if sn[l] + sn[r] < -sn[i]:
                    l += 1

                if sn[l] + sn[r] > -sn[i]:
                    r -= 1

        return list(list_)