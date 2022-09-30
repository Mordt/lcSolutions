class Solution {
    public int[] twoSum(int[] nums, int target) {
        //map each number to its index
        //if index - targen exists in hashmap, return indices
        //otherwise return nothing
        
        //making hashmap
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int[] result = new int[2];
        
        for(int i = 0; i < nums.length; i++){
            
            if(map.containsKey(nums[i] - target)){
                result[0] = i;
                result[1] = map.get(nums[i] - target);
                break;
            } else {
                map.put(nums[i], i);
            }
            
        }
        
        return result;
    }
}
