// DFS_Search.cpp : This file contains the 'main' function. Program execution begins and ends there.
//
#include <queue>
#include <string>
#include <iostream>
using namespace std;

const char travelled = ' ';
const char notTrav = '.';

struct Coords {
  Coords(int r, int c) : row(r), col(c) {}
  int row;
  int col;
};

void explore(string maze[], int currRow, int currCol, queue<Coords>& coords) {
  if (maze[currRow][currCol] == notTrav) {
    maze[currRow][currCol] = travelled;
    coords.push(Coords(currRow, currCol));
  }
}

bool pathExists(string maze[], int maxR, int maxC, int startR, int startC, int endR, int endC) {
  queue<Coords> coords;
  explore(maze, startR, startC, coords);

  while (!coords.empty()) {
    Coords curr = coords.front();
    if (curr.row == endR && curr.col == endC) {
      return true;
    }
    coords.pop();
    explore(maze, curr.row - 1, curr.col, coords);
    explore(maze, curr.row + 1, curr.col, coords);
    explore(maze, curr.row, curr.col + 1, coords);
    explore(maze, curr.row, curr.col - 1, coords);
  }
  return false;
}

int main()
{
  string maze[10] = {
      "XXXXXXXXXX",
      "X........X",
      "XX.X.XXXXX",
      "X..X.X...X",
      "X..X...X.X",
      "XXXX.XXX.X",
      "X.X....XXX",
      "X..XX.XX.X",
      "X...X....X",
      "XXXXXXXXXX"
  };

  if (pathExists(maze, 10, 10, 6, 4, 1, 1))
    cout << "Solvable!" << endl;
  else
    cout << "Out of luck!" << endl;

  for (int i = 0; i < 10; i++) {
    for (int j = 0; j < 10; j++) {
      cout << maze[i][j];
    }
    cout << endl;
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
