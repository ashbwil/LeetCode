class Solution {
    public boolean isPalindrome(int x) {
        int reverse = 0;
        int save = x;
        while (x != 0){
            int y = x % 10;
            x = x / 10;
            reverse = reverse * 10 + y;
        }
    if ((reverse != save || reverse < 0)){
            return false;
        }
        else return true;
    }
}