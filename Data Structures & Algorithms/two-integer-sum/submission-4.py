
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i , n in enumerate(nums):
            tar=target-n
            if tar in seen:
                return[seen[tar], i]
            seen[n]=i
        