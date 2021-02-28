// Компилировать в BC  модель памяти - tiny
// включить в астройках инструкции 386
#include <conio.h>

void SetVideoMode(int m)
{
   asm{
    mov ax,m
    int 10h
   }
}
int GetKey1(void)
{
int key;
asm{  mov ax,0100h
      int 16h
      mov key,ax
  }
  return key;
}
void SetPallete(char *pal)
{
   asm{
	   push si
	   mov si,pal
	   mov dx,03c8h
	   xor   ax,ax
	   out   dx,al
	   mov   cx,768
	   inc   dl
	   rep   outsb
	   pop si
   }
}
// В этой процедуре по идее должны быть Выши гениальные
// высокооптимизированные опусы
void Inner(void)
{
 asm{  push es
 mov ax,0a000h
 mov es,ax    // в es сегмент видеобуффера
 mov bx,64000
 }
 label:
 asm{
 mov ax,bx
 or al,ah
 mov [es:bx],al
 dec bx
 jnz label
 pop es
 }
}

void main()
{
	 char pal[768];
	 int i;
	 // палитра - 256 градаций серого
	 for(i=0;i<256;i++)
	 {
	  pal[i*3]=i;
	  pal[i*3+1]=i;
	  pal[i*3+2]=i;
	 }
	 SetVideoMode(0x13); // Установили вдеорежим и палитру
	 SetPallete(pal);

	 while (!kbhit())
	 {
	Inner();
	 }
	SetVideoMode(3);
}