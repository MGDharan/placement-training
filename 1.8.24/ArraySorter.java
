public class ArraySorter {

    public static void sortArray(int[] arr) {
        java.util.Arrays.sort(arr);
    }

    public static void printArray(int[] arr) {
        System.out.print("[");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
            if (i < arr.length - 1) {
                System.out.print(", ");
            }
        }
        System.out.println("]");
    }

    public static void main(String[] args) {
        int[] numbers = {5, 2, 9, 1, 5, 6};
        System.out.print("Unsorted array: ");
        printArray(numbers);
        sortArray(numbers);
        System.out.print("Sorted array: ");
        printArray(numbers);
    }
}