// Online C++ compiler to run C++ program online
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

    int ec = 0, oc = 0;
    for (int i = 0; i < n; i++)
    {
        if (a[i] % 2 == 0)
        {
            ec++;
        }
        else
        {
            oc++;
        }
    }

    int even[ec], odd[oc];
    int ei = 0, oi = 0;
    for (int i = 0; i < n; i++)
    {
        if (a[i] % 2 == 0)
        {
            even[ei++] = a[i];
        }
        else
        {
            odd[oi++] = a[i];
        }
    }

    for (int i = 0; i < ec; i++)
    {
        cout << even[i] << " ";
    }
    cout << endl;

    for (int i = 0; i < oc; i++)
    {
        cout << odd[i] << " ";
    }

    return 0;
}