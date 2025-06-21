public class VowelCounter {

    public static int countVowels(String str) {
        int count = 0;
        String vowels = "AEIOUaeiou";
        for (int i = 0; i < str.length(); i++) {
            if (vowels.indexOf(str.charAt(i)) != -1) {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        String str = "Hello World";
        int vowelCount = countVowels(str);
        System.out.println("Number of vowels: " + vowelCount);
    }
}