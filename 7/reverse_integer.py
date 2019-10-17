class Solution {
    public int reverse(int x) {
        int back = 0;
        while (x != 0){
            int y = x % 10;
            x = x/10;
            if (back > Integer.MAX_VALUE/10 || (back == Integer.MAX_VALUE / 10 && y > 7)) return 0;
            if (back < Integer.MIN_VALUE/10 || (back == Integer.MIN_VALUE && y < -8))
return 0;
            back = back*10 + y;
        }
        return back;
    }
}