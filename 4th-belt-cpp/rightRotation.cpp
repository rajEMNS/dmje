#include <iostream>
using namespace std;
int main()
{
    int n, d;
    cin >> n >> d;

    int a[n];
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }

    d = d % n;
    d = n - d;

    for (int i = 0, j = d - 1; i < j; i++, j--)
    {
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }
    for (int i = d, j = n - 1; i < j; i++, j--)
    {
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }
    for (int i = 0, j = n - 1; i < j; i++, j--)
    {
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }

    for (int i = 0; i < n; i++)
    {
        cout << a[i] << " ";
    }
    return 0;
}