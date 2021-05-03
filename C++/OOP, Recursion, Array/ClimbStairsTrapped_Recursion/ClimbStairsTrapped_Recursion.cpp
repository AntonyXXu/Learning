// ClimbStairsTrapped_Recursion.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;

bool helper(const int stairs[], const int length, bool visited[], int current) {
  if (current >= length) {
    return true;
  }
  if (current < 0 || stairs[current] == 0 || visited[current] == true) {
    return false;
  }
  visited[current] = true;

  return helper(stairs, length, visited, current - stairs[current]) ||
    helper(stairs, length, visited, current + stairs[current]);
  
}

bool climbable(int stairs[], int length) {
  if (length < 0) {
    return false;
  }
  bool* visited = new bool[length];

  for (int i = 0; i < length; i++) {
    visited[i] = false;
  }
  
  bool ans = helper(stairs, length, visited, 0);
  delete[] visited;
  return ans;

}


int main()
{
  int arr1[5] = { 2,0,3,0,0 };
  cout << climbable(arr1, 5) << endl;
  int arr2[6] = { 1,2,4,1,0,0 };
  cout << climbable(arr2, 6) << endl;
  int arr3[8] = { 4,0,0,1,2,1,1,0 };
  cout << climbable(arr3, 8) << endl;

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
