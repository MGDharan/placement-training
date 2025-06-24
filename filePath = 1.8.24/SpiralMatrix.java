public class  SpiralMatrix{
    public static void printSpiral(int[][] matrix){
        int top = 0, bottom = matrix.length -1, left = 0, right = matrix[0].length -1;
        int dir = 0; // 0: right, 1: down, 2: left, 3: up
        while(top <= bottom && left <= right){
            if(dir == 0){
                for(int i = left; i <= right; i++){
                    System.out.print(matrix[top][i] + " ");
                }
                top++;
            } else if(dir == 1){
                for(int i = top; i <= bottom; i++){
                    System.out.print(matrix[i][right] + " ");
                }
                right--;
            } else if(dir == 2){
                for(int i = right; i >= left; i--){
                    System.out.print(matrix[bottom][i] + " ");
                }
                bottom--;
            } else if(dir == 3){
                for(int i = bottom; i >= top; i--){
                    System.out.print(matrix[i][left] + " ");
                }
                left++;
            }
            dir = (dir + 1) % 4;
        }
    }
    public static void main(String[] args){
        int[][] matrix = {{1,2,3},{4,5,6},{7,8,9}};
        printSpiral(matrix);
    }
}