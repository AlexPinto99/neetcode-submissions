class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k==0: return False
        i, j, l = 0, k, k
        while l>0:
            while j < len(nums):
                if nums[i] == nums[j]:
                    return True
                i, j = i+1, j+1
            l -= 1
            j, i = l, 0
        return False
        