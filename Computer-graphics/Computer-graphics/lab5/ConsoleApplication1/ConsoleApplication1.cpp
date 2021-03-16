#include <windows.h>
#include <iostream>
#include <string>
#include <cmath>
#include <vector>

#include <stdlib.h>
#include <stdio.h>
#include <locale.h>
#include <conio.h>


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
        arr[i][0] = round(x * cos(angle) - y * sin(angle));
        arr[i][1] = round(x * sin(angle) + y * cos(angle));
    }
}

vector<vector<int>> ellipse2(int x, int y, int a, int b, int color = RGB(0, 255, 255))
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

/*
    ЦДА
*/
void singleEndedDDA(double x1, double y1, double x2, double y2, vector<vector<int>> &arr) {

    double px = x2 - x1;
    double py = y2 - y1;

    pushArr(arr, x1, y1);
    if (abs(px) >= abs(py)) {
        double diff = py / px;
        if (x1 <= x2) {
            while (x1 < x2) {
                x1 += 1;
                y1 += diff;
                pushArr(arr, x1, y1);
            }
        }
        else {
            while (x1 > x2) {
                x1--;
                y1 -= diff;
                pushArr(arr, x1, y1);
            }
        }
    }
    else {
        double diff = px / py;
        if (y1 >= y2) {
            while (y1 > y2) {
                y1--;
                x1 -= diff;

                pushArr(arr, x1, y1);
            }
        }
        else {
            while (y1 < y2) {
                y1++;
                x1 += diff;

                pushArr(arr, x1, y1);
            }
        }
    }
}

void ClearConsole()
{
    HANDLE handle = GetStdHandle(STD_OUTPUT_HANDLE);
    CONSOLE_SCREEN_BUFFER_INFO csbi;
    COORD coord = { 0, 0 };
    DWORD written;
    if (GetConsoleScreenBufferInfo(handle, &csbi))
    {
        DWORD nChars = csbi.dwSize.X * csbi.dwSize.Y;
        FillConsoleOutputCharacter(handle, ' ', nChars, coord, &written);
        FillConsoleOutputAttribute(handle, csbi.wAttributes, nChars, coord,
            &written);
    }
    SetConsoleCursorPosition(handle, coord);
}
/*
    РИсует курсор
*/
void cursor(HDC hDC, int x, int y) {
    MoveToEx(hDC, x + 5, y, NULL);
    LineTo(hDC, x - 5, y);
    MoveToEx(hDC, x, y + 5, NULL);
    LineTo(hDC, x, y - 5);
}
/*
    Стирает курсор
*/
void clrcur(HDC hDC, int x, int y) {
    MoveToEx(hDC, x + 5, y, NULL);
    LineTo(hDC, x - 5, y);
    MoveToEx(hDC, x, y + 5, NULL);
    LineTo(hDC, x, y - 5);
}


void printArr(vector<vector<int>>& arr) {

    for (int i = 0; i < arr.size(); i++) {
        for (int j = 0; j < arr[0].size(); j++) {
            cout << arr[i][j] << " " << arr[i][j] << endl;
        }
    }
}


int main()
{
    // int cxSize = 1000;
    // int cySize = 1000;
    // HWND consoleWindow = GetConsoleWindow();
    // SetWindowPos(consoleWindow, HWND_TOP, 0, 0, cxSize, cySize, NULL);
    // 
    // HDC consoleDC = GetDC(consoleWindow);
    // // установка режима и начала координат
    // SetMapMode(consoleDC, MM_LOMETRIC);
    // SetViewportOrgEx(consoleDC, cxSize / 2, cySize / 2, NULL);
    // system("cls");
    // 
    // vector<vector<int>> arr = ellipse2(consoleDC, 0, 0, 300, 600, RGB(0, 255, 255));
    // 
    // 
    // while (true) {
    //     system("cls");
    //     turn(arr, 1);
    //     printArr(consoleDC, arr);
    //     Sleep(5);
    // }

    vector<vector<int>> arr;
    char ch = 'n';
    POINT crd, cur;
    RECT rcCli;
    HDC hDC = GetDC(GetConsoleWindow());
    HPEN PenWhite = CreatePen(PS_SOLID, 2, RGB(255, 255, 255));
    HPEN PenBlack = CreatePen(PS_SOLID, 2, RGB(0, 0, 0));
    HPEN PenBlue = CreatePen(PS_SOLID, 2, RGB(0, 255, 255));
    SelectObject(hDC, PenWhite);
    crd.x = 0;
    crd.y = 0;
    cur.x = 0;
    cur.y = 0;
    // размеры окна
    GetClientRect(WindowFromDC(hDC), &rcCli);
    // размеры клиента
    int nWidth = rcCli.right - rcCli.left; // ширина
    int nHeight = rcCli.bottom - rcCli.top; // высота

    SetMapMode(hDC, MM_LOMETRIC);
    SetViewportOrgEx(hDC, nWidth / 2, nHeight / 2, NULL);

    // прорисовка осей
    /*MoveToEx(hDC, 0, nHeight / 2, NULL);
    LineTo(hDC, nWidth, nHeight / 2);
    MoveToEx(hDC, nWidth / 2, 0, NULL);
    LineTo(hDC, nWidth / 2, nHeight); */

    MoveToEx(hDC, 0, 0, NULL);
    do {
        _getch_nolock();
        if (GetAsyncKeyState(VK_DOWN)) {
            SelectObject(hDC, PenBlack);
            clrcur(hDC, cur.x, cur.y);
            SelectObject(hDC, PenWhite);
            cur.y -= 10;
            MoveToEx(hDC, cur.x, cur.y, NULL);
            cursor(hDC, cur.x, cur.y);
        }
        if (GetAsyncKeyState(VK_UP)) {
            SelectObject(hDC, PenBlack);
            clrcur(hDC, cur.x, cur.y);
            SelectObject(hDC, PenWhite);
            cur.y += 10;
            MoveToEx(hDC, cur.x, cur.y, NULL);
            cursor(hDC, cur.x, cur.y);
        }
        if (GetAsyncKeyState(VK_LEFT)) {
            SelectObject(hDC, PenBlack);
            clrcur(hDC, cur.x, cur.y);
            SelectObject(hDC, PenWhite);
            cur.x -= 10;
            MoveToEx(hDC, cur.x, cur.y, NULL);
            cursor(hDC, cur.x, cur.y);
        }
        if (GetAsyncKeyState(VK_RIGHT)) {
            SelectObject(hDC, PenBlack);
            clrcur(hDC, cur.x, cur.y);
            SelectObject(hDC, PenWhite);
            cur.x += 10;
            MoveToEx(hDC, cur.x, cur.y, NULL);
            cursor(hDC, cur.x, cur.y);
        }
        if (GetAsyncKeyState(VK_SPACE)) {
            SelectObject(hDC, PenBlue);
            MoveToEx(hDC, crd.x, crd.y, NULL);
            LineTo(hDC, cur.x, cur.y);
            singleEndedDDA(crd.x, crd.y, cur.x, cur.y, arr);
            crd.x = cur.x;
            crd.y = cur.y;
        }
        if (GetAsyncKeyState(VK_LCONTROL)) {  // ` или ё перед этим нажать LCNTRL
            
            //printArr(arr);
            while (true) {
                system("cls");
                turn(arr, 1);
                printArr(hDC, arr);
                Sleep(5);
            }
        }
    } while (!GetAsyncKeyState(VK_ESCAPE));
    return 0;


}
