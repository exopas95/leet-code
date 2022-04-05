class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        nums.forEachIndexed { index, _ ->
            for(j in index+1 until nums.size) {
                val result = nums[index] + nums[j]

                if (result == target) {
                    return intArrayOf(index, j)
                }
            }
        }
        return intArrayOf()
    }
}