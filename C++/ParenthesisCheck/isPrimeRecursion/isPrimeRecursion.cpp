// isPrimeRecursion.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
bool isPrime_helper(int n, int denom) {
  if (n <= 1 || denom <= 1) {
    return true;
  }

  if (n % denom == 0) {
    return false;
  }

  return isPrime_helper(n, denom - 1);
}

bool isPrime(int n) {
  return isPrime_helper(n, n / 2);
}



int main()
{
  std::cout << isPrime(1) << std::endl;
  std::cout << isPrime(17) << std::endl;
  std::cout << isPrime(256) << std::endl;
  std::cout << isPrime(377) << std::endl;
  std::cout << isPrime(113) << std::endl;
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
