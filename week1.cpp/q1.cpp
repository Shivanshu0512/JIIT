#include <stdio.h>

int main() {
    int n, i;
    float sum = 0.0, average;

    printf("Enter the number of elements: ");
    scanf("%d", &n);

    int arr[n];
    printf("Enter the elements: ");
    for (i = 0; i < n; ++i) {
        scanf("%d", &arr[i]);
        sum += arr[i];
    }

    average = sum / n;
    printf("Average = %.2f\n", average);

    return 0;
}