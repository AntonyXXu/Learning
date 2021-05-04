// StackTemplate.cpp : This file contains the 'main' function. Program execution begins and ends there.
// 
// Build a Template Stack class using a linked list with push, pop, top, empty
//

#include <iostream>
using namespace std;

template <typename T>
class Stack {
public:
  Stack();
  void push(T data);
  void pop();
  T top();
  bool isEmpty();
  ~Stack();
private:
  struct Node {
    T data;
    Node* next;
  };
  Node* m_head;
};
template <typename T>
Stack<T>::Stack() {
  m_head = nullptr;
}
template <typename T>
Stack<T>::~Stack() {
  while (m_head != nullptr) {
    Node* del = m_head;
    m_head = m_head->next;
    delete del;
  }
}
template <typename T>
void Stack<T>::push(T data) {
  Node newNode = new Node();
  newNode.data = data;
  newNode.next = m_head;
  m_head = newNode;  
}
template <typename T>
void Stack<T>::pop() {
  Node* del = m_head;
  m_head = del->next;
  delete del;
}

template <typename T>
bool Stack<T>::isEmpty() {
  return m_head == nullptr;
}

template <typename T>
T Stack<T>::top() {
  if (m_head != nullptr) {
    return m_head->val;
  }
  return T();
}

int main()
{
    std::cout << "Hello World!\n";
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
