#include <iostream>
using namespace std;

void insertionSort(int arr[], int n)
{
    for (int i = 1; i < n; i++)
    {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

int main()
{
    int n1;
    cin >> n1;
    int a1[n1];
    for (int i = 0; i < n1; i++)
    {
        cin >> a1[i];
    }

    int n2;
    cin >> n2;
    int a2[n2];
    for (int i = 0; i < n2; i++)
    {
        cin >> a2[i];
    }

    int n = n1 + n2;
    int merged[n];

    for (int i = 0; i < n1; i++)
    {
        merged[i] = a1[i];
    }
    for (int i = 0; i < n2; i++)
    {
        merged[n1 + i] = a2[i];
    }

    insertionSort(merged, n);
    for (int i = 0; i < n; i++)
    {
        cout << merged[i] << " ";
    }

    return 0;
}
