class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        table = {}
        for i in nums:
            if i in table:
                return True
            table[i] = True
        return False