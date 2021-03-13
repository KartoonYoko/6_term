#include <windows.h>
#include <iostream>
#include <string>
#include <cmath>
#include <vector>


using namespace std;

void pushArr(vector<vector<int>>& arr, int x, int y) {
    vector<int> sub;
    sub.push_back(x);
    sub.push_back(y);
    arr.push_back(sub);
}

void printArr(HDC cnsl, vector<vector<int>> arr, int color = RGB(0, 255, 255)) {
    for (int i = 0; i < arr.size(); i++) {
        SetPixel(cnsl, arr[i][0], arr[i][1], color);
    }
}

/*
* Матрица поворота
    M =
    [cosO  -sinO
     sinO  cosO]
     double aRad = 180*angle/3.1415;
     double rMx[2][2] = ((Math.Cos(aRad),-Math.Sin(aRad)),(Math.Sin(aRad),Math.Cos(aRad));
*/
void turn(vector<vector<int>>& arr, int angle) {
    angle = 180 * angle / 3.1415;
    for (int i = 0; i < arr.size(); i++) {
        int x = arr[i][0];
        int y = arr[i][1];
        arr[i][0] = (x * cos(angle) - y * sin(angle));
        arr[i][1] = (x * sin(angle) + y * cos(angle));
    }
}

vector<vector<int>> ellipse2(HDC cnsl, int x, int y, int a, int b, int color = RGB(0, 255, 255))
{
    vector<vector<int>> res;
    int col, i, row, bnew;
    long a_square, b_square, two_a_square, two_b_square, four_a_square, four_b_square, d;

    b_square = b * b;
    a_square = a * a;
    row = b;
    col = 0;
    two_a_square = a_square << 1;
    four_a_square = a_square << 2;
    four_b_square = b_square << 2;
    two_b_square = b_square << 1;
    d = two_a_square * ((row - 1) * (row)) + a_square + two_b_square * (1 - a_square);
    while (a_square * (row) > b_square * (col))
    {
        //SetPixel(cnsl, col + x, row + y, color);
        //SetPixel(cnsl, col + x, y - row, color);
        //SetPixel(cnsl, x - col, row + y, color);
        //SetPixel(cnsl, x - col, y - row, color);
        pushArr(res, col + x, row + y);
        pushArr(res, col + x, y - row);
        pushArr(res, x - col, row + y);
        pushArr(res, x - col, y - row);
        
        if (d >= 0)
        {
            row--;
            d -= four_a_square * (row);
        }
        d += two_b_square * (3 + (col << 1));
        col++;
    }
    d = two_b_square * (col + 1) * col + two_a_square * (row * (row - 2) + 1) + (1 - two_a_square) * b_square;
    while ((row)+1)
    {
        //SetPixel(cnsl, col + x, row + y, color);
        //SetPixel(cnsl, col + x, y - row, color);
        //SetPixel(cnsl, x - col, row + y, color);
        //SetPixel(cnsl, x - col, y - row, color);
        pushArr(res, col + x, row + y);
        pushArr(res, col + x, y - row);
        pushArr(res, x - col, row + y);
        pushArr(res, x - col, y - row);

        if (d <= 0)
        {
            col++;
            d += four_b_square * col;
        }
        row--;
        d += two_a_square * (3 - (row << 1));
    }

    return res;
}


int main()
{
    HWND consoleWindow = GetConsoleWindow();
    HDC consoleDC = GetDC(consoleWindow);
    system("cls");

    vector<vector<int>> arr = ellipse2(consoleDC, 400, 300, 50, 100, RGB(0, 255, 255));

    //printArr(consoleDC, arr);
    //turn(arr, 0);
    //printArr(consoleDC, arr);
    while (true) {
        turn(arr, 90);
        printArr(consoleDC, arr);
        Sleep(500);
    }

}
