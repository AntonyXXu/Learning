// Return the number of ways that all n1 elements of a1 appear in
// the n2 element array a2 in the same order (though not necessarily
// consecutively).  The empty sequence (i.e. one where n1 is 0)
// appears in a sequence of length n2 in 1 way, even if n2 is 0.
// For example, if a2 is the 7 element array
//	10 50 40 20 50 40 30
// then for this value of a1     the function must return
//	10 20 40			1
//	10 40 30			2
//	20 10 40			0
//	50 40 30			3

#include <iostream>
using namespace std;

int countIsIn(const double a1[], int n1, const double a2[], int n2) {
  if (n1 == 0) {
    return 1;
  }
  if (n2 < n1) {
    return 0;
  }

  int sum = countIsIn(a1, n1, a2 + 1, n2 - 1);
  if (a1[0] == a2[0]) {
    sum += countIsIn(a1 + 1, n1 - 1, a2 + 1, n2 - 1);
  }
  return sum;
}


int main()
{
  double x1[3] = { 50, 40, 30 };
  double x2[3] = { 10, 20, 40 };
  double x3[3] = { 20, 10, 40 };
  double a2[7] = { 10, 50, 40, 20, 50, 40, 30 };

  cout << countIsIn(x1, 3, a2, 7) << endl;
  cout << countIsIn(x2, 3, a2, 7) << endl;
  cout << countIsIn(x3, 3, a2, 7) << endl;
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
