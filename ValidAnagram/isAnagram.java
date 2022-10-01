class Solution {
    public boolean isAnagram(String s, String t) {
        //approach is to sort both, if the same, return true
        String[] sArray = new String[]{s};
        String[] tArray = new String[]{t};
        
        String[] sPrime = Arrays.sort(sArray);
        String[] tPrime = Arrays.sort(tArray);
        
        if(sPrime == tPrime){
            return true;
        } else {
            return false;
        }
    }
}
