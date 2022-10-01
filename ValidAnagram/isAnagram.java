class Solution {
    public boolean isAnagram(String s, String t) {
        //approach is to sort both, if the same, return true
        char[] sArray = s.toCharArray();
        char[] tArray = t.toCharArray();
        
        if(Arrays.sort(sArray) == Arrays.sort(tArray)){
            return true;
        } else {
            return false;
        }
    }
}
