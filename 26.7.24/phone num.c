int isValidPhoneNumber(int num) {
    char numStr[20];
    sprintf(numStr, "%d", num);
    
    if (numStr[0] != '0') {
        for (int i = 0; numStr[i] != '\0'; i++) {
            if (numStr[i] < '0' || numStr[i] > '9') {
                return 0;
            }
        }
        return 1;
    }

    return 0;
}

int main() {
    int n, x;
    printf("Enter the number of items: ");
    scanf("%d", &n);
    printf("Enter the cost of each item: ");
    scanf("%d", &x);
    int totalBill = n * x;
    if (isValidPhoneNumber(totalBill)) {
        printf("Yes\n");
    } else {
        printf("No\n");
    }

    return 0;
}
