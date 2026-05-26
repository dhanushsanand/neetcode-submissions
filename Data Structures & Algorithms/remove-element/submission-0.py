class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        currentIndex = 0
        for index, num in enumerate(nums):
            if num != val:
                k+=1
                nums[currentIndex] = num
                currentIndex +=1
        return k