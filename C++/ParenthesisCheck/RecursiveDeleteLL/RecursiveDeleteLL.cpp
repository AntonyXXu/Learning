// RecursiveDeleteLL.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

struct Node {
  int val;
  Node* next;
};
class List {
public:
  List();
  void insert(int val);
  void deleteList();
  void deleteRecursion()
private:
  Node* m_head;
};
List::List() {
  m_head = nullptr;
}

void List::insert(int val) {
  Node* ptr = new Node;
  ptr->val = val;
  ptr->next = m_head;
  m_head = ptr;
}

void List::deleteList() {
  while (m_head != nullptr) {
  Node* del = m_head;
  m_head = m_head->next;
  delete del;
  }
  int a = 1;
}

void List::deleteRecursion() {

}

int main()
{
  List a = List();
  for (int i = 0; i < 5; i++)
  {
    a.insert(i * i);
  }
  a.deleteList();
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
