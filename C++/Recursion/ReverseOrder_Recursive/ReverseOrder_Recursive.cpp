// ReverseOrder_Recursive.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;

void swap(double& a, double& b) {
  double temp = a;
  a = b;
  b = temp;
}

// Rearrange the elements of the array so that all the elements
   // whose value is > divider come before all the other elements,
   // and all the elements whose value is < divider come after all
   // the other elements.  Upon return, firstNotGreater is set to the
   // index of the first element in the rearranged array that is
   // <= divider, or n if there is no such element, and firstLess is
   // set to the index of the first element that is < divider, or n
   // if there is no such element.
   // In other words, upon return from the function, the array is a
   // permutation of its original value such that
   //   * for 0 <= i < firstNotGreater, a[i] > divider
   //   * for firstNotGreater <= i < firstLess, a[i] == divider
   //   * for firstLess <= i < n, a[i] < divider
   // All the elements > divider end up in no particular order.
   // All the elements < divider end up in no particular order.

void div(double arr[], int n, double divider, int& firstNotGreater, int& firstLess) {
  if (n < 0) {
    n = 0;
  }

  firstNotGreater = 0;
  firstLess = n;
  int firstUnknown = 0;
  while (firstUnknown < firstLess)
  {
    if (arr[firstUnknown] < divider)
    {
      firstLess--;
      exchange(arr[firstUnknown], arr[firstLess]);
    }
    else
    {
      if (arr[firstUnknown] > divider)
      {
        exchange(arr[firstNotGreater], arr[firstUnknown]);
        firstNotGreater++;
      }
      firstUnknown++;
    }
  }
}

void sort(double arr[], int n) {
  if (n <= 1) {
    return;
  }
  int firstNotGreater;
  int firstLess;

  div(arr, n, arr[0], firstNotGreater, firstLess);
  sort(arr, firstNotGreater);
  sort(arr + firstLess, n - firstLess);
}