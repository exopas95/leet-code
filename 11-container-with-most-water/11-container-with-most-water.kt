class Solution {
    fun maxArea(height: IntArray): Int {
        var max = 0
        var left = 0
        var right = height.lastIndex
        
        while (left < right) {
            max = Math.max(max, Math.min(height[left], height[right]) * (right-left))
            if (height[left] > height[right]) {
                right--
            } else {
                left++
            }
        }
        return max
    }
}