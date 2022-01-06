class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers) - 1):
            l = numbers[i]
            r = target - l
            
            try:
                return [i+1, (len(numbers)-numbers[::-1].index(r))]
            except:
                pass