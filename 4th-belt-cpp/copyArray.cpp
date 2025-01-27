#include <iostream>
using namespace std;
int main()
{

    int n;
    cin >> n;

    int a[n];
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }

    int c[n];
    for (int i = 0; i < n; i++)
    {
        c[i] = a[i];
    }

    for (int i = 0; i < n; i++)
    {
        cout << c[i] << " ";
    }

    return 0;
}