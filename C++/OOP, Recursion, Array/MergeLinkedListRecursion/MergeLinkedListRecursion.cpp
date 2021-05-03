// MergeLinkedListRecursion.cpp : This file contains the 'main' function. Program execution begins and ends there.
// Merge two sorted linked lists in order, without allocating any new nodes

#include <iostream>
using namespace std;

struct Node {
  int val;
  Node* next;
};

Node* merge(Node* h1, Node* h2) {
  if (h1 == nullptr) {
    return h2;
  }
  if (h2 == nullptr) {
    return h1;
  }
  if (h1->val <= h2->val) {
    h1->next = merge(h1->next, h2);
    return h1;
  }
  else {
    h2->next = merge(h1, h2->next);
    return h2;
  }
}

void printList(Node* head) {
  if (head == nullptr) {
    return;
  }
  cout << head->val << "\t";
  printList(head->next);
}


int main()
{
  //Initialize two list
  Node* h1 = new Node;
  h1->val = 1;
  h1->next = new Node;
  h1->next->val = 3;
  h1->next->next = new Node;
  h1->next->next->val = 7;
  h1->next->next->next= new Node;
  h1->next->next->next->val = 10;
  h1->next->next->next->next = nullptr;
  Node* h2 = new Node;
  h2->val = 0;
  h2->next = new Node;
  h2->next->val = 5;
  h2->next->next = new Node;
  h2->next->next->val = 7;
  h2->next->next->next = new Node;
  h2->next->next->next->val = 9;
  h2->next->next->next->next = nullptr;

  Node* res = merge(h1, h2);
  printList(res);
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
