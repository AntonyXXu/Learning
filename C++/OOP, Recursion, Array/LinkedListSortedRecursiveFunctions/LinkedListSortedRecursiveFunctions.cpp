// LinkedListSortedRecursiveFunctions.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;
struct Node {
  int val;
  Node* next;
};

Node* insert(Node* head, int num) {
  if (head == nullptr || head->val > num) {
    Node* newNode = new Node;
    newNode->val = num;
    newNode->next = head;
    head = newNode;
  }
  else {
    head->next = insert(head->next, num);
  }
  return head;
}

void printReverse(Node* head) {
  if (head == nullptr) {
    return;
  }
  printReverse(head->next);
  cout << head->val;
}

int main()
{
  Node* p = nullptr;  
  Node* result = insert(p, 1);
  result = insert(result, 5);
  result = insert(result, -5);
  
  printReverse(result);
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
