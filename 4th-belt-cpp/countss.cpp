#include <iostream>
using namespace std;
int main()
{
    string s;
    getline(cin, s);

    int alpha = 0;
    int digit = 0;
    int special = 0;
    for (char c : s)
    {
        if (isalpha(c))
        {
            alpha++;
        }
        else if (isdigit(c))
        {
            digit++;
        }
        else
        {
            special++;
        }
    }
    cout << alpha << " " << digit << " " << special << endl;
    return 0;
}