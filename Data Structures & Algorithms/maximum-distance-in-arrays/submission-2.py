class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mini, maxi = min(arrays[0]), max(arrays[0])
        diff = 0
        for i in range(1, len(arrays)):
            temp_min = min(arrays[i])
            temp_max = max(arrays[i])
            temp_diff = max(abs(temp_max - mini), abs(maxi-temp_min))
            diff = max(temp_diff, diff)
            if temp_min < mini: mini = temp_min
            if temp_max > maxi: maxi = temp_max
        return diff
