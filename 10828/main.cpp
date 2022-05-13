// (BOJ -10828) 스택: https://www.acmicpc.net/problem/10828

#include <iostream>

using namespace std;

class Node {
private:
    int data;
    Node *next;
public:
    Node(int data) {
        this->data = data;
        this->next = nullptr;
    }

    void setNext(Node *next) {
        this->next = next;
    }

    int getData() {
        return data;
    }

    Node *getNext() {
        return this->next;
    }
};

class SinglyLinkedList {
private:
    Node *head;
    Node *tail;
    int size;
public:
    SinglyLinkedList() {
        head = nullptr;
        tail = nullptr;
        size = 0;
    }

    bool isEmpty() {
        return head == nullptr;
    }

    Node *getHead() {
        return this->head;
    }

    void appendFront(int data) {
        size++;
        Node *node = new Node(data);
        if (isEmpty()) {
            head = node;
            tail = node;
        } else {
            node->setNext(head);
            head = node;
        }
    }

    int removeFront() {
        if (isEmpty())
            return -1;
        else {
            size--;
            int old;
            if (head == tail) {
                old = tail->getData();
                head = nullptr;
                tail = nullptr;
            } else {
                old = head->getData();
                head = head->getNext();
            }
            return old;
        }
    }

    int getSize() {
        return this->size;
    }
};

class LinkedStack {
private:
    SinglyLinkedList *sll;
public:
    LinkedStack() {
        sll = new SinglyLinkedList();
    }

    void push(int data) {
        sll->appendFront(data);
    }

    int empty() {
        if (sll->isEmpty()) return 1;
        else return 0;
    }

    int top() {
        if (sll->isEmpty()) return -1;
        return sll->getHead()->getData();
    }

    int pop() {
        return sll->removeFront();
    }

    int size() {
        return sll->getSize();
    }
};

int main() {
    LinkedStack *ls = new LinkedStack();
    int N;
    cin >> N;
    for (int i = 0; i < N; i++) {
        string operation;
        cin >> operation;
        if (operation == "push") {
            int data;
            cin >> data;
            ls->push(data);
        } else if (operation == "top") {
            cout << ls->top() << endl;
        } else if (operation == "pop") {
            cout << ls->pop() << endl;
        } else if (operation == "size") {
            cout << ls->size() << endl;
        } else {
            cout << ls->empty() << endl;
        }
    }
    return 0;
}