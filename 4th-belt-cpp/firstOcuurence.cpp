#include <iostream>
#include <string>
using namespace std;

int main()
{
    string S, W;
    getline(cin, S);
    getline(cin, W);

    int lenS = S.length();
    int lenW = W.length();

    int start = -1;

    for (int i = 0; i <= lenS - lenW; ++i)
    {
        int j;
        for (j = 0; j < lenW; ++j)
        {
            if (S[i + j] != W[j])
            {
                break;
            }
        }
        if (j == lenW)
        {
            start = i;
            break;
        }
    }

    if (start != -1)
    {
        for (int k = start; k < lenS - lenW; ++k)
        {
            S[k] = S[k + lenW];
        }

        lenS -= lenW;
        S[lenS] = '\0';
    }

    int startTrim = 0;
    while (startTrim < lenS && S[startTrim] == ' ')
    {
        startTrim++;
    }

    int endTrim = lenS - 1;
    while (endTrim >= 0 && S[endTrim] == ' ')
    {
        endTrim--;
    }

    for (int i = startTrim; i <= endTrim; ++i)
    {
        cout << S[i];
    }
    cout << endl;

    return 0;
}