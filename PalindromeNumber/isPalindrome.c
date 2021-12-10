//solution to palindrome number question

bool isPalindrome(int x){
    
    //all negative numbers are not palindromes.
    if(x < 0){
        return false;
    }
    
    //reverse x and store in y
    int toRev = x;
    int remainder;
    long y = 0;
    
    while(toRev != 0){
        remainder = toRev % 10;//obtain remainder of x
        y = (long) y * 10 + remainder;//typecast as some numbers overflow
        toRev /= 10;
    }
    
    //check if x is the same as y.
    x = (long) x;
    if(x == y){
        return true;
    } else {
        return false;
    }
}
