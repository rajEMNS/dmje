#include <iostream>
#include <climits>
using namespace std;
int main()
{
    string s;
    getline(cin, s);

    int min = INT_MAX;
    int max = INT_MIN;

    int f[256] = {0};
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] != ' ')
        {
            f[(int)s[i]]++;
        }
    }

    for (int i = 0; i < 256; i++)
    {
        if (f[i] > 0)
        {
            if (f[i] > max)
            {
                max = f[i];
            }

            if (f[i] < min)
            {
                min = f[i];
            }
        }
    }

    cout << "Highest Frequency" << endl;
    for (int i = 0; i < 256; i++)
    {
        if (f[i] == max)
        {
            cout << (char)i << " ";
        }
    }
    cout << max << endl;

    cout << "Lowest frequency" << endl;
    for (int i = 0; i < 256; i++)
    {
        if (f[i] == min)
        {
            cout << (char)i << " ";
        }
    }
    cout << min << endl;

    return 0;
}