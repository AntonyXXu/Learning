#include <iostream>
using namespace std;

bool solvable(int a, int b, int c) {
  if (c == 0) {
    return true;
  }
  if (c < 0) {
    return false;
  }
  return solvable(a, b, c - a) || solvable(a, b, c - b);

}

int main() {
  cout << solvable(7, 5, 45) << endl;
  cout << solvable(1, 3, 40) << endl;
  cout << solvable(9, 23, 112) << endl;
}