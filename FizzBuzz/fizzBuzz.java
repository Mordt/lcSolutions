class Solution {
    public List<String> fizzBuzz(int n) {
        
        List<String> result = new List<String>();
        if(n % 3 == 0 && n% 5 == 0){
            result = "FizzBuzz";
        } else if(n % 3 == 0){
            result = "Fizz";
        } else if(n % 5 == 0){
            result = "Buzz";
        } else {
            result = n.toString();
        }
        return result;
    }
}
