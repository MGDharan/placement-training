public class  RightPascalTriangle{
    public static void printRightPascal(int n){
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n - i; j++){
                System.out.print(" ");
            }
            for(int j = 0; j <= i; j++){
                System.out.print(combination(i,j) + " ");
            }
            System.out.println();
        }
    }
    public static int combination(int n, int r){
        if(r > n) return 0;
        if(r == 0 || r == n) return 1;
        return combination(n-1, r-1) + combination(n-1, r);
    }
    public static void main(String[] args){
        printRightPascal(5);
    }
}