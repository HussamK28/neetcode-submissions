class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            current = nums[i]
            complement = target - current
            if complement in hashmap:
                return [hashmap[complement], i]
            else:
                hashmap[current] = i
        
        return [-1,-1]
        