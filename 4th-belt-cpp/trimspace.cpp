#include <iostream>
using namespace std;

int main()
{
    string x;
    getline(cin, x);
    int start = 0;
    int end = x.length() - 1;
    while (start < x.length() && isspace(x[start]))
    {
        start++;
    }
    while (end > x.length() && isspace(x[end]))
    {
        end--;
    }

    for (int i = start; i <= end; i++)
    {
        cout << x[i];
    }

    return 0;
}