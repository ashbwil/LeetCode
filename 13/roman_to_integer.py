class Solution {
    public int romanToInt(String s) {
         int n = s.length()-1;
        int solution = 0;
        int number = 0;
        int prevNum = 0;

        while (n >= 0) {
            char letter = s.charAt(n);

            switch(letter){
                case 'I' : number = 1;
                    break;
                case 'V' : number = 5;
                    break;
                case 'X' : number = 10;
                    break;
                case 'L' : number = 50;
                    break;
                case 'C' : number = 100;
                    break;
                case 'D' : number = 500;
                    break;
                case 'M' : number = 1000;
                    break;
            }
            if (prevNum == 0 || prevNum < number){
                solution = solution + number;
            }
            else if (prevNum == number){
                solution = solution + number;
            }
            else if(prevNum > number){
                solution = solution - number;
            }
            prevNum = number;

            n--;
        }
        return solution;
    }
}