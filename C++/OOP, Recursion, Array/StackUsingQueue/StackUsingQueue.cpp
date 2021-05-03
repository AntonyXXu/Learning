// StackUsingQueue.cpp : This file contains the 'main' function. Program execution begins and ends there.
//
#include <queue>
#include <iostream>
using namespace std;
class Stk {
public:
  bool empty();
  int size();
  int top();
  void pop();
  void push(int val);
private:
  queue<int> m_storage;
};

bool Stk::empty() {
  return size() == 0;
}
int Stk::size() {
  return m_storage.size();
}
int Stk::top() {
  return m_storage.back();
}
void Stk::pop() {
  for (int i = 0; i < m_storage.size() - 1; i++) {
    int val = m_storage.front();
    m_storage.push(val);
    m_storage.pop();
  }
  m_storage.pop();
}
void Stk::push(int val) {
  m_storage.push(val);
}


int main()
{
  Stk s;
  for (int i = 0; i < 10; i++) {
    s.push(i);
  }
  cout << s.size() << endl;;
  while (!s.empty()) {
    cout << s.top() << endl;
    s.pop();
  }

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
