class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hMap = {}
        for i in range(len(nums)):
            if nums[i] in hMap and i-hMap[nums[i]]<= k:
                return True
            hMap[nums[i]] = i
        return False
        