class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        result = []
        # result.append(pairs) # Removed to avoid premature appending
        for i in range(len(pairs)):
            j = i
            while j > 0 and pairs[j].key < pairs[j-1].key:
                temp = pairs[j]
                pairs[j] = pairs[j-1]
                pairs[j-1] = temp
                j -= 1
            result.append(list(pairs))
        return result