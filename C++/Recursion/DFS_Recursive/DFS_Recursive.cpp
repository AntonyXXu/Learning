// DFS_Recursive.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
using namespace std;

const char travelled = ' ';
const char notTrav = '.';

bool pathExists(string maze[], int maxR, int maxC, int startR, int startC, int endR, int endC) {
  if (startR == endR && startC == endC) {
    return true;
  }

  if (maze[startR][startC] == notTrav) {
    maze[startR][startC] = travelled;
    return pathExists(maze, maxR, maxC, startR - 1, startC, endR, endC)
      || pathExists(maze, maxR, maxC, startR + 1, startC, endR, endC)
      || pathExists(maze, maxR, maxC, startR, startC - 1, endR, endC)
      || pathExists(maze, maxR, maxC, startR, startC + 1, endR, endC);
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

  if (pathExists(maze, 10, 10, 6, 4, 8, 8))
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