public class  DiagonalTraversal{
    public static void printDiagonal(int[][] matrix){
        int rows = matrix.length;
        int cols = matrix[0].length;
        for(int k = 0; k < rows + cols -1; k++){
            int i = 0;
            int j = k;
            while(i < rows && j >=0){
                System.out.print(matrix[i][j] + " ");
                i++;
                j--;
            }
            System.out.println();
        }
    }
    public static void main(String[] args){
        int[][] matrix = {{1,2,3},{4,5,6},{7,8,9}};
        printDiagonal(matrix);
    }
}