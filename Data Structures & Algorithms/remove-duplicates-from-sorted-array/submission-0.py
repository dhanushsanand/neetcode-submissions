class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        currentElement = nums[0]
        currentIndex = 1
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != currentElement:
                k +=1
                currentElement = nums[i]
                nums[currentIndex] = nums[i]
                currentIndex +=1
        return k