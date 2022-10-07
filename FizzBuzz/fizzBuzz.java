class Solution {
    public List<String> fizzBuzz(int n) {
        
        List<String> result = new ArrayList<String>();
        
        for(i = 1; i <= n; i++){
            if(i % 3 == 0 && i % 5 == 0){
                result.set(i, "FizzBuzz");
            } else if(i % 3 == 0){
                result.set(i, "Fizz");
            } else if(i % 5 == 0){
                result.set(i, "Buzz");
            } else {
                result.set(i, n.toString());
            }
        }
        return result;
    }
}
