#include <windows.h>
#include <iostream>
#include <string>
#include <cmath>

using namespace std;


void enter(double& x, double& y, double& r) {
    cout << "Enter x: ";
    cin >> x;
    cout << "Enter y: ";
    cin >> y;
    cout << "Enter r: ";
    cin >> r;
}

void circle(double x0, double y0, double radius, HDC cnsl) {

    double x = 0;
    double y = radius;

    double del1 = pow(x + 1, 2) + pow(y - 1, 2) - pow(radius, 2);
    double del2 = pow(x + 1, 2) + pow(y, 2) - pow(radius, 2);
    double del = del1 + del2;

    double u = 4 * x + 6;
    double v = 4 * (x - y) + 10;

    while ((x != y) && (x + 1 != y) && (x - 1 != y)) {
        SetPixel(cnsl, x0 + x, y0 - y, RGB(0, 255, 255));
        SetPixel(cnsl, x0 + y, y0 - x, RGB(0, 255, 255));
        SetPixel(cnsl, x0 + y, y0 + x, RGB(0, 255, 255));
        SetPixel(cnsl, x0 + x, y0 + y, RGB(0, 255, 255));
        SetPixel(cnsl, x0 - x, y0 + y, RGB(0, 255, 255));
        SetPixel(cnsl, x0 - y, y0 + x, RGB(0, 255, 255));
        SetPixel(cnsl, x0 - y, y0 - x, RGB(0, 255, 255));
        SetPixel(cnsl, x0 - x, y0 - y, RGB(0, 255, 255));


        if (del <= 0) {
            x++;
            u += 4;
            v += 4;
            del += u;
        }
        else {
            x++;
            y--;
            u += 4;
            v += 8;
            del += v;
        }
    }
}

void ellipse(double x0, double y0, double radius, HDC cnsl) {
    
    double x = 0;
    double y = radius;

    double del = 0;

    double b = radius / 2;
    double u = 12 * b;
    double v = 12 * b + 8 * radius;

    double l = b * radius;

    while (l > 0) {
        SetPixel(cnsl, x0 + x, y0 - y, RGB(0, 255, 255));
        // SetPixel(cnsl, x0 + y, y0 - x, RGB(0, 255, 255));
        // SetPixel(cnsl, x0 + y, y0 + x, RGB(0, 255, 255));
        // SetPixel(cnsl, x0 + x, y0 + y, RGB(0, 255, 255));
        // SetPixel(cnsl, x0 - x, y0 + y, RGB(0, 255, 255));
        // SetPixel(cnsl, x0 - y, y0 + x, RGB(0, 255, 255));
        // SetPixel(cnsl, x0 - y, y0 - x, RGB(0, 255, 255));
        // SetPixel(cnsl, x0 - x, y0 - y, RGB(0, 255, 255));


        if (del <= 0) {
            x++;
            del += u;
            u += 8 * b;
            v += 8 * (b + radius);           
            
            l -= b;
            //cout << del << endl;
        }
        else {
            x++;
            y--;    
            del += v;
            u += 4;
            v += 8;
            
            l -= (b + radius);
            //cout << del << endl;
        }
    }
}


void ellipse2(HDC cnsl, int x, int y, int a, int b, int color)
{
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
        SetPixel(cnsl, col + x, row + y, color);
        SetPixel(cnsl, col + x, y - row, color);
        SetPixel(cnsl, x - col, row + y, color);
        SetPixel(cnsl, x - col, y - row, color);
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
        SetPixel(cnsl,col + x, row + y, color);
        SetPixel(cnsl,col + x, y - row, color);
        SetPixel(cnsl,x - col, row + y, color);
        SetPixel(cnsl,x - col, y - row, color);
        if (d <= 0)
        {
            col++;
            d += four_b_square * col;
        }
        row--;
        d += two_a_square * (3 - (row << 1));
    }
}


int main()
{
    HWND consoleWindow = GetConsoleWindow();
    HDC consoleDC = GetDC(consoleWindow);
    system("cls");
    string ch = "s";

    while (ch != "end") {

        double x2;
        double y2;
        double r;
        cout << "Enter data: " << endl;
        enter(x2, y2, r);

        system("cls");
        // circle(x2, y2, r, consoleDC);
        ellipse(x2, y2, r, consoleDC);
        //ellipse2(consoleDC, 400, 300, 100, 50, RGB(0, 255, 0));
        cout << "Enter \"end\" to finish painting: " << endl;
        cin >> ch;
        system("cls");
    }
}

