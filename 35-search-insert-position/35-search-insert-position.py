class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        first, end = 0, len(nums)-1
        
        while first <= end:
            mid = (first + end) // 2
            
            if target == nums[mid]:
                return mid
            
            elif target > nums[mid]:
                first = mid + 1
                
            elif target < nums[mid]:
                end = mid - 1
                
        return first