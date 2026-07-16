class Solution {
    public int[] searchRange(int[] nums, int target) {
        int leftIdx = findleft(nums, target);
        int rightIdx= findright(nums, target);
        return new int[] {leftIdx, rightIdx};
    }
    private int findleft(int[] nums, int target){
        int res = -1;
        int st = 0;
        int en = nums.length -1;
        while(st <= en){
            int mid = st + (en - st)/2;
            if(nums[mid] == target){
                res = mid;
                en = mid -1;
            } else if (target < nums[mid]){
                en = mid -1;
            } else {
                st = mid + 1;
            }
        }
        return res;
    }
        private int findright(int[] nums, int target){
        int res = -1;
        int st = 0;
        int en = nums.length -1;
        while(st <= en){
            int mid = st + (en - st)/2;
            if(nums[mid] == target){
                res = mid;
                st = mid +1;
            } else if (target < nums[mid]){
                en = mid -1;
            } else {
                st = mid + 1;
            }
        }
        return res;
    }
}