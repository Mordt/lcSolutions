class Solution {
    public boolean isAnagram(String s, String t) {
  
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
