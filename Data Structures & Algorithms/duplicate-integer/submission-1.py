class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for index, val in enumerate(nums):
            if hash_map.get(val) == None:
                hash_map[val] = 1
            else:
                return True
        return False