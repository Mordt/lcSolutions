class Solution {
    public List<String> fizzBuzz(int n) {
        
        List<String> result = new List<String>();
        if(n % 3 == 0 && n% 5 == 0){
            result[n] = "FizzBuzz";
        } else if(n % 3 == 0){
            result[n] = "Fizz";
        } else if(n % 5 == 0){
            result[n] = "Buzz";
        } else {
            result[n] = n.toString();
        }
        return result;
    }
}
