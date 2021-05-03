// LinkedListRecursion.cpp : This file contains the 'main' function. Program execution begins and ends there.
//
// reverse a doubly linked list

#include <iostream>
using namespace std;
struct Node {
  int val;
  Node* next;
  Node* prev;
};

Node* reverse(Node* head) {
  if (head == nullptr) {
    return head;
  }
  Node* temp = head->prev;
  head->prev = head->next;
  head->next = temp;
  if (head->prev == nullptr) {
    return head;
  }
  return reverse(head->prev);

}


int main()
{
  Node* p = new Node;
  p->val = 1;
  p->prev = nullptr;
  p->next = new Node;
  p->next->val = 2;
  p->next->prev = p;
  p->next->next = nullptr;
  Node* t = reverse(p);
  cout << p->val << endl;
  cout << t->val << endl;

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
