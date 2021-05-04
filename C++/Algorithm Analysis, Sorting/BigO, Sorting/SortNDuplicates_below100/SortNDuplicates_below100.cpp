// SortNDuplicates_below100.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

int randomSum(int n) {
  int counter = 0;
  int sum = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < i; j++) {
      if (rand() % 2 == 1) {
        sum += 1;
      }
      for (int k = 0; k < j * i; k += j) {
        counter += 1;
        if (rand() % 2 == 2) {
          sum += 1;
        }
      }
    }
  }
  return counter;
}


int main()
{
  std::cout << randomSum(1) << std::endl;
  std::cout << randomSum(2) << std::endl;
  std::cout << randomSum(3) << std::endl;
  std::cout << randomSum(4) << std::endl;
  std::cout << randomSum(1000) << std::endl;
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
