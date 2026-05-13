class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        if len(nums) != 0:
            max_num = max(nums)
        else: return k

        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = max_num + 1
            else:
                k += 1
        nums.sort()


        return k