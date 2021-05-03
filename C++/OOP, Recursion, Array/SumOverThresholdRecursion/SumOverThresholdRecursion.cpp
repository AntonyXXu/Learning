// SumOverThresholdRecursion.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

//Rewrite the following function recursively.You can add new parametersand
//completely change the function implementation, but you can’t use loops.
//
//This function sums the numbers of an array from left to right until the sum
//exceeds some threshold.At that point, the function returns the running sum.
//Returns - 1 if the threshold is not exceeded before the end of the array is
//reached.
//int sumOverThreshold(int x[], int length, int threshold) {
//  int sum = 0;
//  for (int i = 0; i < length; i++) {
//    sum += x[i];
//    if (sum > threshold) {
//      return sum;
//    }
//  }
//  return -1;
//}


#include <iostream>
using namespace std;

int helper(int x[], int length, int threshold, int sum, int index) {
  if (sum >= threshold) {
    return sum;
  }
  if (sum < threshold && length <= 0) {
    return -1;
  }
  if (length == 1) {
    return sum + x[index] >= threshold ? sum : -1;
  }
  return helper(x, length - 1, threshold, sum + x[index], index + 1);
}

int sumOverThreshold(int x[], int length, int threshold) {
  int sum = 0;
  int index = 0;
  return helper(x, length, threshold, sum, index);
}


int main()
{
  int arr[5] = { 1,3,5,7,9 };
  cout << sumOverThreshold(arr, 5, 15) << endl;
  cout << sumOverThreshold(arr, 5, 90) << endl;
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
