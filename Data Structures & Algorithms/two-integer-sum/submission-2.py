class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, num in enumerate(nums):
            complement = target - num
            if num == complement and num in hashMap:
                return [hashMap[complement], i]
            hashMap[num] = i
            if complement in hashMap and hashMap[complement] != i:
                return [hashMap[complement], i]
        return []
        