class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, value in enumerate(nums):
            diff = target - value
            if diff in hashmap:
                return [hashmap[diff],i]
            hashmap[value] = i

        # for i in range(len(nums)):
        #     if nums[i] in hashmap:
        #         return [hashmap[nums[i]],i]
        #     diff = target - nums[i]
        #     hashmap[diff] = i