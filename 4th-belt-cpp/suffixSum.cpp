using namespace std;
#include <iostream>

int main()
{

    int n;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }

    int arr[n];
    int sum = 0;
    for (int i = n - 1; i >= 0; i--)
    {
        sum += a[i];
        arr[i] = sum;
    }

    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }

    return 0;
}