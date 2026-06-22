class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(index, current_xor):
            # Base case, when we reach the end of the array
            if index == len(nums):
                return current_xor
            # Exclude
            exclude = backtrack(index+1, current_xor)
            # Include
            include = backtrack(index+1, current_xor^nums[index])

            # Summing up the totals from the choices
            return exclude + include

        return backtrack(0,0)
        