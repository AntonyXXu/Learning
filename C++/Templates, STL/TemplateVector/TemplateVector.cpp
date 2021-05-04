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
  T arr[] = 
  m_size = 0;
  m_capacity = 1;
}
template<typename T>
Vector<T>::~Vector() {
  delete[] m_arr;
}

template<typename T>
void Vector<T>::pushBack(T data) {
  if (m_size == m_capacity) {
    m_capacity *= 2;
    T* newArr = new T[m_capacity];
    for (int i = 0; i < m_size; i++) {
      newArr[i] = m_arr[i];
    }
    delete[] m_arr;
    m_arr = newArr;
  }
  m_arr[m_size] = data;
  m_size++;
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
