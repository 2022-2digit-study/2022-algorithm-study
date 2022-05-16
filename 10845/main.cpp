// (BOJ - 10828) https://www.acmicpc.net/problem/10828
#include <iostream>

using namespace std;

class Queue {
private:
    int *arr;
    int head_idx;
    int tail_idx;
    int size;
public:
    Queue(int size) {
        this->head_idx = 0;
        this->tail_idx = 0;
        this->arr = new int[size];
        this->size = size;
    }

    bool isEmpty() {
        return this->head_idx == this->tail_idx;
    }

    int front() {
        if (isEmpty()) {
            return -1;
        }
        return this->arr[head_idx % this->size];
    }

    int back() {
        if (isEmpty())
            return -1;
        return this->arr[(tail_idx - 1) % this->size];
    }

    void push(int data) {
        arr[tail_idx % this->size] = data;
        tail_idx++;
    }

    int pop() {
        if (isEmpty())
            return -1;
        head_idx++;
        return this->arr[(head_idx - 1) % this->size];
    }

    int len() {
        return tail_idx - head_idx;
    }
};


int main() {
    int N;
    cin >> N;
    Queue *q = new Queue(N);
    for (int i = 0; i < N; i++) {
        string operation;
        cin >> operation;
        if (operation == "push") {
            int data;
            cin >> data;
            q->push(data);
        } else if (operation == "front") {
            cout << q->front() << endl;
        } else if (operation == "pop") {
            cout << q->pop() << endl;
        } else if (operation == "back") {
            cout << q->back() << endl;
        } else if (operation == "size") {
            cout << q->len() << endl;
        } else {
            cout << int(q->isEmpty()) << endl;
        }
    }
    return 0;
}
