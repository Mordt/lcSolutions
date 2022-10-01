class Solution {
    public boolean isAnagram(String s, String t) {
        
        if(s.length() != t.length()){
            return false;
        }
  
        char[] sArray = s.toCharArray();
        char[] tArray = t.toCharArray();

        Arrays.sort(sArray);
        Arrays.sort(tArray);
        
        boolean result = true;
        for(int i = 0; i < sArray.length; i++){
            if(sArray[i] != tArray[i]){
                result = false;
            }
        }
        return result;

    }
}
