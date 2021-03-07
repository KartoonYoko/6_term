#include <windows.h>
#include <iostream>
#include <string>
#include <cmath>

using namespace std;


void enter(double& x, double& y) {
    cout << "Enter x: ";
    cin >> x;
    cout << "Enter y: ";
    cin >> y;
}

/*
    ЦДА
*/
void singleEndedDDA(double x1, double y1, double x2, double y2, HDC cnsl) {

    double px = x2 - x1;
    double py = y2 - y1;

    SetPixel(cnsl, x1, y1, RGB(0, 255, 255));
    if (abs(px) >= abs(py)) {
        double diff = py / px;
        if (x1 <= x2) {
            while (x1 < x2) {
                x1 += 1;
                y1 += diff;
                SetPixel(cnsl, x1, y1, RGB(0, 255, 255)); // blue
            }
        }
        else {
            while (x1 > x2) {
                x1--;
                y1 -= diff;
                SetPixel(cnsl, x1, y1, RGB(0, 255, 255)); // blue
            }
        }
    }
    else {
        double diff = px / py;
        if (y1 >= y2) {
            while (y1 > y2) {
                y1--;
                x1 -= diff;

                SetPixel(cnsl, x1, y1, RGB(0, 255, 255)); // blue
            }
        }
        else {
            while (y1 < y2) {
                y1++;
                x1 += diff;

                SetPixel(cnsl, x1, y1, RGB(0, 255, 255)); // blue
            }
        }
    }
}

/*
    Брезенхем
*/
void bresenhamDDA(double x1, double y1, double x2, double y2, HDC cnsl) {
    double px = x2 - x1;
    double py = y2 - y1;
    
   
    SetPixel(cnsl, x1, y1, RGB(0, 255, 255));
    if (abs(px) >= abs(py)) {
        double diff = py - px;
        double e = 2 * px - py;
        for (int i = 0; i < px; i++) {
            if (e >= 0) {
                x1++;
                y1++;
                e += 2 * diff;
            }
            else {
                x1++;
                e += 2 * py;
            }
            SetPixel(cnsl, x1, y1, RGB(0, 255, 0)); // green
        }
        //cout << px << "; " << py << endl;
    }
    else {
        double diff = px - py;
        double e = 2 * py - px;
        for (int i = 0; i < py; i++) {
            if (e >= 0) {
                x1++;
                y1++;
                e += 2 * diff;
            }
            else {
                y1++;
                e += 2 * px;
            }
            SetPixel(cnsl, x1, y1, RGB(0, 255, 0)); // green
            //cout << "x: " << x1 << "; y: " << y1 << endl;
        }
        //cout << px << "; " << py << endl;
    }
}

int main() 
{
    HWND consoleWindow = GetConsoleWindow();
    HDC consoleDC = GetDC(consoleWindow);
    system("cls");
    string ch = "s";

    // смещение для любого из методов, чтобы видеть два графика
    int offset = 10;

    while (ch != "end") {
        double x1;
        double y1;
        cout << "Enter first point: " << endl;
        enter(x1, y1);
        double x2;
        double y2;
        cout << "Enter second point: " << endl;
        enter(x2, y2);

        system("cls");
        bresenhamDDA(x1, y1, x2, y2, consoleDC);
        singleEndedDDA(x1 + offset, y1 + offset, x2 + offset, y2 + offset, consoleDC);

        cout << "Enter \"end\" to finish painting: " << endl;
        cin >> ch;
        system("cls");
    }
}

