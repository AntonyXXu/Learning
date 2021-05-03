// DeleteOddSumSetList.cpp : This file contains the 'main' function. Program execution begins and ends there.
// With a set of pointers to a list of integers, delete all the odd-summed lists and return the number of lists
// that are removed.

#include <iostream>
#include <set>
#include <list>
using namespace std;

int deleteOddSumLists(set <list <int>*>& st) {
  set<list<int>*>::iterator setItr;
  setItr = st.begin();
  int numDeleted = 0;
  while (setItr != st.end()) {
    list<int>::iterator listItr;
    listItr = (*setItr)->begin();
    int sum = 0;
    while (listItr != (*setItr)->end()){
      sum += (*listItr);
      listItr++;
  }
    if (sum % 2 != 0) {
      setItr = st.erase(setItr);
      numDeleted++;
    }
    else {
      setItr++;
    }    
  }
  return numDeleted;
}

// Sample driver code:
int main()
{
  set<list<int>*> s;
  list<int>* l1 = new list<int>;
  l1->push_back(1);
  l1->push_back(2);
  list<int>* l2 = new list<int>;;
  l2->push_back(1);
  l2->push_back(1);
  list<int>* l3 = new list<int>;;
  l3->push_back(1);
  l3->push_back(0);
  s.insert(l1);
  s.insert(l2);
  s.insert(l3);
  cout << deleteOddSumLists(s) << endl;
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
