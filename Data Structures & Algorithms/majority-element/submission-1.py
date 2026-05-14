class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}
        for i in range(len(nums)):
            hashMap[nums[i]] = 1 + hashMap.get(nums[i], 0)
            if hashMap[nums[i]] >= len(nums)/2:
                return nums[i]


