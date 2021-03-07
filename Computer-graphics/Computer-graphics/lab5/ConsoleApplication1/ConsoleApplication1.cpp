#include <iostream>
#include <Windows.h>
#include <stdio.h>


using namespace std;

/*
* Матрица поворота
    M = 
    [cosO  -sinO
     sinO  cosO]
     double aRad = 180*angle/3.1415;
     double rMx[2][2] = ((Math.Cos(aRad),-Math.Sin(aRad)),(Math.Sin(aRad),Math.Cos(aRad));
*/
int main()
{
    HANDLE const hStdInput = GetStdHandle(STD_INPUT_HANDLE);

    DWORD Mode;
    GetConsoleMode(hStdInput, &Mode);
    SetConsoleMode(hStdInput, Mode | ENABLE_MOUSE_INPUT);

    for (;;)
    {
        WaitForSingleObject(hStdInput, INFINITE);

        INPUT_RECORD InRec;
        DWORD NumEvents;
        BOOL b = ReadConsoleInputW(hStdInput, &InRec, 1, &NumEvents);

        if ((0 != NumEvents) && (MOUSE_EVENT == InRec.EventType))
        {
            DWORD const BtnState = InRec.Event.MouseEvent.dwButtonState;

            if (BtnState & FROM_LEFT_1ST_BUTTON_PRESSED)
            {
                cout << "LEFT BUTTON" << endl;
            }

            if (BtnState & RIGHTMOST_BUTTON_PRESSED)
            {
                cout << "RIGHT BUTTON" << endl;
            }
        }
    }

    return 0;
}

LRESULT APIENTRY MainWndProc(HWND hwndMain, UINT uMsg,
    WPARAM wParam, LPARAM lParam)
{
    HDC hdc;                       // дескриптор контекста устройства
    RECT rcClient;                 // прямоугольник клиентской области
    POINT ptClientUL;              // верхний левый угол клиент.области
    POINT ptClientLR;              // нижний правый угол клиент.области
    static POINTS ptsBegin;        // начальная точка
    static POINTS ptsEnd;          // новая конечная точка
    static POINTS ptsPrevEnd;      // предыдущая конечная точка
    static BOOL fPrevLine = FALSE; // флаг предыдущей линии

    switch (uMsg)
    {
    case WM_LBUTTONDOWN:

        // Захватываем мышку.

        SetCapture(hwndMain);

        // Получаем экранные координаты клиентской области,
        // и преобразуем их в клиентские координаты.

        GetClientRect(hwndMain, &rcClient);
        ptClientUL.x = rcClient.left;
        ptClientUL.y = rcClient.top;

        // Добавляем один пиксель справа и снизу, так как координаты,
        // полученные из GetClientRect не включают левого и
        // нижнего пикселей.

        ptClientLR.x = rcClient.right + 1;
        ptClientLR.y = rcClient.bottom + 1;
        ClientToScreen(hwndMain, &ptClientUL);
        ClientToScreen(hwndMain, &ptClientLR);

        // Копируем клиентские координаты клиентской области
        // в структуру rcClient. Ограничиваем курсор мышки клиентской
        // областью, передав структуру rcClient в
        // функцию ClipCursor.

        SetRect(&rcClient, ptClientUL.x, ptClientUL.y,
            ptClientLR.x, ptClientLR.y);
        ClipCursor(&rcClient);

        // Преобразуем координаты курсора для структуры POINTS,
        // которая определяет начальную точку рисования линии
        // в течение сообщения WM_MOUSEMOVE.

        ptsBegin = MAKEPOINTS(lParam);
        return 0;

    case WM_MOUSEMOVE:

        // Чтобы рисовалась линия, то при движении мышки
        // пользователь должен удерживать нажатой левую кнопку мышки.

        if (wParam & MK_LBUTTON)
        {

            // Получаем контекст устройства (DC) для клиентской области

            hdc = GetDC(hwndMain);

            // Следующая функция гарантирует, что пиксели
            // предыдущей линии установлены в белый цвет, а
            // вновь нарисованной линии - в чёрный.

            SetROP2(hdc, R2_NOTXORPEN);

            // Если линия была нарисована в предыдущем WM_MOUSEMOVE,
            // то рисуем поверх неё. Тем самым, установив пиксели
            // линии в белый цвет, мы сотрём её.

            if (fPrevLine)
            {
                MoveToEx(hdc, ptsBegin.x, ptsBegin.y, (LPPOINT)NULL);
                LineTo(hdc, ptsPrevEnd.x, ptsPrevEnd.y);
            }

            // Преобразуем текущие координаты курсора в структуру
            // POINTS, а затем рисуем новую линию.

            ptsEnd = MAKEPOINTS(lParam);
            MoveToEx(hdc, ptsBegin.x, ptsBegin.y, (LPPOINT)NULL);
            LineTo(hdc, ptsEnd.x, ptsEnd.y);

            // Устанавливаем флаг предыдущей линии, сохраняем конечную
            // точку новой линии, а затем освобождаем DC.

            fPrevLine = TRUE;
            ptsPrevEnd = ptsEnd;
            ReleaseDC(hwndMain, hdc);
        }
        break;

    case WM_LBUTTONUP:

        // Пользователь закончил рисовать линию. Сбрасываем флаг
        // предыдущей линии, освобождаем курсор мышки и
        // освобождаем захват мышки.

        fPrevLine = FALSE;
        ClipCursor(NULL);
        ReleaseCapture();
        return 0;

    case WM_DESTROY:
        PostQuitMessage(0);
        break;

        // Обрабатываем другие сообщения.

    }
}