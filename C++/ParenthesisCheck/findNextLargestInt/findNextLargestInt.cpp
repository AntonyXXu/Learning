// findNextLargestInt.cpp : This file contains the 'main' function. Program execution begins and ends there.
/***************************************
  Write a function findNextInts that takes in two integer arrays sequence and
  results, along with the size of both of them, which is n.This function assumes
  that sequence already contains a sequence of positive integers.For each
  position i(from 0 to n - 1) of sequence, this function should find the smallest j
  such that j > iand sequence[j] > sequence[i], and put sequence[j] in results[i]; if
  there is no such j, put - 1 in sequence[i].Try to do this without nested for loops
  both iterating over the array!
  void findNextInts(const int sequence[], int results[], int n);
  Example:
  int seq[] = { 2, 6, 3, 1, 9, 4, 7 }; // Only positive integers!
  int res[7];
  findNextInt(seq, res, 7);
  for (int i = 0; i < 7; i++) { // Should print: 6 9 9 9 -1 7 -1
    cout << res[i] << " ";
  }
  cout << endl;
******************************************/

#include <iostream>
using namespace std;

void findNextInts(const int seq[], int res[], int n)
{
  if (n <= 0) return;
  bool found = false;
  for (int i = 0; i < n; i++) {
    int val = seq[i];
    found = false;
    for (int j = i + 1; j < n; ++j) {
      int s = seq[j];
      if (seq[j] > val) {
        res[i] = seq[j];
        found = true;
        break;
      }
    }
    if (!found) {
      res[i] = -1;
    }
  }
  res[n - 1] = -1;
}

int main()
{
  int seq[] = { 2, 6, 3, 1, 9, 4, 7 }; // Only positive integers!
  int res[7];
  findNextInts(seq, res, 7);
  for (int i = 0; i < 7; i++) {
    // Should print: 6 9 9 9 -1 7 -1
    cout << res[i] << " ";
  }
  cout << endl;
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
