// ClassInheritance.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
using namespace std;
class A {
public:
  A() : m_val(0) {
    cout << "What a wonderful world! " << m_val << endl;
  }
  virtual ~A() { cout << "Guess this is goodbye " << endl; }
  virtual void saySomething() = 0;
  virtual int giveMeSomething() = 0;
private:
  int m_val;
};
class B : public A {
public:
  B() : m_str("me"), m_val(1) {
    cout << m_str << " has just been birthed." << endl;
  }
  B(string str, int val) : m_str(str), m_val(val) {
    cout << "More complex birth " << m_str << endl;
  }
  ~B() {
    cout << "Why do I have to leave this world!" << endl;
  }
  virtual void saySomething() {
    cout << "Coming in from " << m_str << " with "
      << giveMeSomething() << endl;
  }
  virtual int giveMeSomething() { return m_val * 5; }
private:
  int m_val;
  string m_str;
};
class C {
public:
  C() : m_val(2) {
    m_b = new B("C", m_val);
    cout << "Hello World!!" << endl;
  }
  C(B b, int val) : m_val(val) {
    m_b = new B(b);
    cout << m_b->giveMeSomething() << endl;
  }
  ~C() {
    m_b->saySomething();
    delete m_b;
    cout << "Goodbye world!" << endl;
  }
private:
  B* m_b;
  int m_val;
};
int main() {
  B* b_arr = new B[5];
  for (int i = 0; i < 5; i++) {
    b_arr[i].saySomething();
  }
  B b("B", 5);
  A* a = &b;
  cout << a->giveMeSomething() << endl;
  C c;
  C c2(b, b.giveMeSomething());
  delete[] b_arr;
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
