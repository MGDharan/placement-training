public class  DecimalToBinary{
    public static String decimalToBinary(int decimal){
        return Integer.toBinaryString(decimal);
    }
    public static void main(String[] args){
        System.out.println(decimalToBinary(11));
    }
}