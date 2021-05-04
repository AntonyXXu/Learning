// SortNDuplicates_below100.cpp : This file contains the 'main' function. Program execution begins and ends there.
// Sort an array of integers, the integers can have duplicates. Also, the integers are between 1 to 100

#include <iostream>

void sort(int arr[], int length) {
  int nums[100] = { 0 };
  for (int i = 0; i < length; i++) {
    int val = arr[i];
    nums[val - 1] += 1;
  }
  int index = 0;
  for (int i = 0; i < length; i++) {
    while (nums[index] == 0) {
      index += 1;
    }
    arr[i] = index + 1;
    nums[index] -= 1;
  }
}


int main()
{
  int arr[10] = { 3,5,12,1,100,59,1,59,5,3 };
  sort(arr, 10);
  for (int i = 0; i < 10; i++) {
    std::cout << arr[i] << std::endl;
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
