class Solution {
    public int[] twoSum(int[] nums, int target) {
        int len = nums.length;
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i=0; i<len; i++){
            int key = target - nums[i];
            if(map.containsKey(key)){
                return new int[] {map.get(key), i};
            } else {
                map.put(nums[i], i);
            }
        }
       
        return new int [] {-1, -1};
        
    }
}