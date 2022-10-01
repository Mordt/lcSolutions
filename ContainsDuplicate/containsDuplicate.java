class Solution {
    public boolean containsDuplicate(int[] nums) {
        //iterate thru, add to map
        //if not in map, continue
        //if in map, return true as contains duplicate
        //else return false
        Set<Integer> set = new HashSet<Integer>();
        boolean result = false;
        
        for(int i = 0; i < nums.length; i++){
            if(map.contains(nums[i])){
                result = true;
            } else {
                map.add(nums[i]);
            }
        }
        return result;
    }
}
