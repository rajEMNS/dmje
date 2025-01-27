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

    int t;
    cin >> t;

    int gc = 0, lc = 0;
    for (int i = 0; i < n; i++)
    {
        if (a[i] > t)
        {
            gc++;
        }
        else
        {
            lc++;
        }
    }

    int greater[gc], lesser[lc];
    int gIndex = 0, lIndex = 0;
    for (int i = 0; i < n; i++)
    {
        if (a[i] > t)
        {
            greater[gIndex++] = a[i];
        }
        else
        {
            lesser[lIndex++] = a[i];
        }
    }

    for (int i = 0; i < gc; i++)
    {
        cout << greater[i] << " ";
    }
    cout << endl;

    for (int i = 0; i < lc; i++)
    {
        cout << lesser[i] << " ";
    }
    return 0;
}