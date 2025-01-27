#include <iostream>
using namespace std;

int main()
{

    string s;
    cin >> s;

    int roundB = 0;
    int curlyB = 0;
    int squareB = 0;

    for (char c : s)
    {
        if (c == '(')
        {
            roundB++;
        }
        else if (c == '{')
        {
            curlyB++;
        }
        else if (c == '[')
        {
            squareB++;
        }
        else if (c == ')')
        {
            roundB--;
            if (roundB < 0)
            {
                cout << "False" << endl;
                return 0;
            }
            else if (curlyB > 0 || squareB > 0)
            {
                cout << "False" << endl;
                return 0;
            }
        }
        else if (c == '}')
        {
            curlyB--;
            if (curlyB < 0)
            {
                cout << "False" << endl;
                return 0;
            }
            else if (roundB > 0 || squareB > 0)
            {
                cout << "False" << endl;
                return 0;
            }
        }
        else if (c == ']')
        {
            squareB--;
            if (squareB < 0)
            {
                cout << "False" << endl;
                return 0;
            }
            else if (roundB > 0 || curlyB > 0)
            {
                cout << "False" << endl;
                return 0;
            }
        }
    }

    if (roundB == 0 && squareB == 0 && curlyB == 0)
    {
        cout << "True" << endl;
    }
    else
    {
        cout << "False" << endl;
    }

    return 0;
}
