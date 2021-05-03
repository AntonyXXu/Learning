// LongestCommonSubstringRecursive.cpp : This file contains the 'main' function. Program execution begins and ends there.
//The function should return the longest common subsequence of characters
//between the two strings s1 and s2.Basically, it should return a maximum
//length string of characters that are common to both strings and are in the
//same order in both strings.
//Example:
//res = longestCommonSubsequence(“tostrings”, “computers”);
//res should contain the string “oes”


#include <iostream>
#include <string>
using namespace std;
string commonSubSeq(string s1, string s2) {
  if (s1.size() <= 0 || s2.size() <= 0) {
    return "";
  }
  if (s1[0] == s2[0]) {
    return s1[0] + commonSubSeq(s1.substr(1), s2.substr(1));
  }
  string res1 = commonSubSeq(s1.substr(1), s2);
  string res2 = commonSubSeq(s1, s2.substr(1));
  return res1.size() >= res2.size() ? res1 : res2;
}

int main()
{
  string s1 = "tostrings";
  string s2 = "computers";
  cout << commonSubSeq(s1, s2) << endl;
  string s3 = "abcd123";
  string s4 = "abd42739";
  cout << commonSubSeq(s3, s4) << endl;
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
