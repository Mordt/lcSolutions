class Solution {
    public boolean containsDuplicate(int[] nums) {
        /*
            iterate thru, add to set
            if not in set, continue
            if in set, return true as contains duplicate
            else return false
        
            Reason for using set is that we can do set.contains
            in constant time. not a hashmap because we dont have
            key->value pairs.
        */

        Set<Integer> set = new HashSet<Integer>();
        boolean result = false;
        
        for(int i = 0; i < nums.length; i++){
            if(set.contains(nums[i])){
                result = true;
            } else {
                set.add(nums[i]);
            }
        }
        return result;
    }
}
