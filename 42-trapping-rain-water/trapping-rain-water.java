class Solution {
    public int trap(int[] height) {
        int left = 0, right = height.length-1, total =0,
         leftmax = height[0], rightmax = height[right];
         while(left < right){
            if(height[left] < height[right]){
                leftmax = Math.max(leftmax, height[left]);
                if(leftmax - height[left] > 0){
                    total+= leftmax - height[left];
                }
                left++;
            } else {
                rightmax = Math.max(rightmax, height[right]);
                if(rightmax - height[right] > 0){
                    total += rightmax - height[right];
                }
                right--;
            }
         }
         return total;
    }
}