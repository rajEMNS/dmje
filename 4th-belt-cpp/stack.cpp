#include <iostream>
#include <string>

using namespace std;

class Stack
{
private:
    int *stack;
    int top;
    int maxSize;

public:
    Stack(int size)
    {
        maxSize = size;
        stack = new int[maxSize];
        top = -1;
    }
    void push(int value)
    {
        if (top < maxSize - 1)
        {
            stack[++top] = value;
        }
        else
        {
            cout << "stack overflow" << endl;
        }
    }

    void pop()
    {
        if (top >= 0)
        {
            cout << stack[top--] << endl;
        }
        else
        {
            cout << "stack underflow" << endl;
        }
    }

    void topElement()
    {
        if (top >= 0)
        {
            cout << stack[top] << endl;
        }
        else
        {
            cout << "stack underflow" << endl;
        }
    }
};

int main()
{
    int N, S;
    cin >> N >> S;

    Stack myStack(S);

    for (int i = 0; i < N; i++)
    {
        string operation;
        cin >> operation;

        if (operation == "push")
        {
            int x;
            cin >> x;
            myStack.push(x);
        }
        else if (operation == "pop")
        {
            myStack.pop();
        }
        else if (operation == "top")
        {
            myStack.topElement();
        }
    }

    return 0;
}