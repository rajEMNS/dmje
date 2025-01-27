#include <iostream>
using namespace std;
class Queue
{
private:
    int front, rear, size;
    int queue[100];

public:
    Queue(int size)
    {
        front = 0;
        rear = 0;
        this->size = size;
    }
    void enqueue(int value)
    {
        queue[rear++] = value;
    }
    int dequeue()
    {
        return queue[front++];
    }
};
int main()
{
    int n;
    cin >> n;
    Queue q(n);
    for (int i = 0; i < n; i++)
    {
        int elements;
        cin >> elements;
        q.enqueue(elements);
    }
    for (int i = 0; i < n; i++)
    {
        cout << q.dequeue() << " ";
    }
    return 0;
}