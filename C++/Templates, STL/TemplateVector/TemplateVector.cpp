// TemplateVector.cpp : This file contains the 'main' function. Program execution begins and ends there.
// Create a Vector Class using Tmplate, with a dynamically allocated array.
// Only implement push_back and constructor, destructor

#include <iostream>

template <typename T>
class Vector {
public: 
  Vector();
  ~Vector();
  void pushBack(T data);
private:
  int m_size;
  int m_capacity;
  T* m_arr;
};

template<typename T>
Vector<T>::Vector() {
  m_size = 0;
    m_capacity = 10;
}


int main()
{
    
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
