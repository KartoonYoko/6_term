// HelloWindowsDesktop.cpp
// compile with: /D_UNICODE /DUNICODE /DWIN32 /D_WINDOWS /c

#include <windows.h>
#include <stdlib.h>
#include <string.h>
#include <tchar.h>

/************************************************************************
                          Лабораторная работа N1

                                Пример 2.

                              HELLOWIN2.CPP

                        Каркасное приложение Windows

************************************************************************/

// Windows и т.п.

/*  Указываем прототип оконной функции (здесь она называется WndProc).
    Тип возвращаемого значения: LRESULT CALLBACK (функция обратного вызова).
    Параметры: дескриптор окна, которому принадлежит функция,
               идентификатор сообщения, переданного функции,
               параметры сообщения (WPARAM и LPAPAM).
*/


LRESULT CALLBACK WndProc(HWND, UINT, WPARAM, LPARAM);


/* Описание функции WinMain():
   Тип возвращаемого значения - WINAPI,
   Параметры:
              HINSTANCE hInst - дескриптор текущего экземпляра приложения,
              HINSTANCE       - не используется (всегда NULL)
              LPSTR           - параметры командной строки
              int             - режим показа окна

   В данном случае используется только первый параметр, поэтому он имеет
   собственное название hInst. Прочие параметры не используются.
*/

int WINAPI WinMain(HINSTANCE hInst, HINSTANCE, LPSTR, int)
{
    WNDCLASS wcl;        // Структура для класса окна
    MSG      msg;        // Структура для хранения переданного сообщения
    HWND     wnd;        // Дескриптор окна


    // Заполнение структуры WNDCLASS - создание класса окна

    wcl.style = 0;                // Стиль окна - по умолчанию
    wcl.lpfnWndProc = WndProc;     // Оконной функцией назначается WndProc
    wcl.hInstance = hInst;        // Дескриптор приложения
    wcl.hCursor = LoadCursor(NULL, IDC_ARROW);  // Форма курсора в окне
    wcl.hIcon = LoadIcon(NULL, IDI_APPLICATION);  // Иконка приложения      
    wcl.hbrBackground = (HBRUSH)(COLOR_WINDOW + 1);  // Цвет фона      
    wcl.lpszMenuName = NULL;                     // Оконного меню нет (NULL)
    wcl.lpszClassName = LPCWSTR("First");            // Имя класса окна
    wcl.cbClsExtra = wcl.cbWndExtra = 0; // Дополнительные параметры (до лампочки)


    if (!RegisterClass(&wcl)) return 0;   // Регистрация класса окна

    // Создание окна
    wnd = CreateWindow
    (
        LPCWSTR("First"),                   // Класс окна
        LPCWSTR("Hello, Windows!"),         // Текст в заголовке окна
        WS_OVERLAPPEDWINDOW,       // Стиль - обычное окно с  рамкой
        CW_USEDEFAULT, CW_USEDEFAULT,  // Координаты и размеры окна - по умолчанию
        CW_USEDEFAULT, CW_USEDEFAULT,
        NULL, NULL,           // Родительского окна и оконного меню нет
        hInst,           // Окно принадлежит приложению с дескриптором hInst     
        NULL
    );           // Дополнительных параметров нет  

    ShowWindow(wnd, SW_SHOW);           // Показ созданного окна


    /*
       Запуск цикла обработки сообщений
       Цикл выполняется до тех пор, пока функция GetMessage(), выбирающая
       сообщения из очереди сообщений приложения, не получит сообщение WM_QUIT,
       сигнализирующее о завершении работы. В этом случае GetMessage()
       возвращает 0, и цикл завершается. Внутри цикла происходит трансляция
       витуальных кодов клавиш посредством вызова TranslateMessage (), затем
       функция DispatchMessage () передает обработанное сообщение обратно
       Windows, которая вызывает установленную при регистрации класса окна
       callback-функцию (в данном случае - WndProc).
    */

    while (GetMessage(&msg, NULL, 0, 0))
    {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    return msg.wParam;
}


/*
    Оконная функция анализирует переданное в параметре MSG сообщение.
    Если поступило сообщение WM_DESTROY (было выбрано закрытие окна),
    то необходимо отправить специальное сообщение о завершении работы
    вызовом PostQuitMessage(). Все прочие сообщение обрабатываются по
    умолчанию самой операционной системой. Для этого они передаются в
    Windows посредством вызова DefWindowProc().
*/
LRESULT CALLBACK WndProc(HWND wnd, UINT msg, WPARAM wp, LPARAM lp)
{
    switch (msg)
    {

    case WM_DESTROY:
        PostQuitMessage(0);
        return 0;

    default:
        return DefWindowProc(wnd, msg, wp, lp);

    }
}