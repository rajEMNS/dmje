#include <iostream>
#include <string>
using namespace std;

int main()
{
    string input, compressed = "";
    cin >> input;

    int count = 1;
    for (int i = 1; i <= input.length(); i++)
    {
        if (i < input.length() && input[i] == input[i - 1])
        {
            count++;
        }
        else
        {
            compressed += input[i - 1] + to_string(count);
            count = 1;
        }
    }

    if (compressed.length() < input.length())
    {
        cout << compressed << endl;
    }
    else
    {
        cout << input << endl;
    }

    return 0;
}