class Solution {
    public boolean isAnagram(String s, String t) {
        //approach is to sort both, if the same, return true
        String sPrime = Arrays.sort(s);
        String tPrime = Arrays.sort(t);
        
        if(sPrime == tPrime){
            return true;
        } else {
            return false;
        }
    }
}
