#include <windows.h>

int WINAPI WinMain(HINSTANCE, HINSTANCE, LPSTR, int)
{
	return MessageBox(NULL, "Hello, Windows!",
		"First Windows Program",
		MB_OK | MB_ICONEXCLAMATION);
}
