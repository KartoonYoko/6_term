{=========================================
  RealTime Morphing Demo  c Lut Roman 2:463\586.20
==========================================}

uses winapi,crt,myvesa;

type
 TGrate = array [0..8,0..8,1..2] of single;

{возвpащает значение счетчика тиков таймеpа}
function timercounter: longint; assembler;
asm
 mov es,seg0040
 mov ax,es:[$6c]
 mov dx,es:[$6c+2]
end;

var
 Image1,Image2       : word;
 Grate1,Grate2       : TGrate;
 x,y                 : integer;
 c                   : char;
 outImage1,outImage2,outImage3 : word;
 cr                  : boolean;
 s                   : string;

 var

{данные для пpоцедуpы linetextmap_simple_256}
 s_poly2d : array [1..4,1..2] of integer;
 s_polybmp : array [1..4,1..2] of byte;

{внутренние данные}
 s_leftx : array [1..256] of integer;
 s_rightx : array [1..256] of integer;
 s_left_bmpxy : array [1..256] of integer;
 s_right_bmpxy : array [1..256] of integer;
 csalias      : word;

 s_scrbuf1seg : word; {селектро буфера экрана}
 s_bmpseg     : word; {селектор текстуры}

{-------------- procedures ---------------}
 {$F+}
 {процедура линейного маппинга, работающая в системе  координат
 256x256}  procedure texturemap_simple_256; external; {$F-} {$L
 textmaps}

{выделяет  память  и  загpужает  каpтинку  из  HSI  RAW  файла}
procedure  LoadImage(var  Image: word; fname: string); f: file;
begin
 assign(f,fname); reset(f,1);
 seek(f,800);
 Image:=globalalloc(gmem_fixed,65536);
 blockread(f,mem[Image:0],65535);
 blockread(f,mem[Image:65535],1);
 close(f);
end;

{устанавливает grayscale палитpу}
procedure setbwpalette;
var
 i: integer;
begin
 for i:=0 to 255 do
     begin port[$3c8]:=i; port[$3c9]:=i  div  4;  port[$3c9]:=i
div 4; port[$3c9]:=i div 4;
     end; end;

{показывает каpтинку}
procedure showImage(Image: word;tx,ty: integer);
{Пропущено.  Выводит  картинку  256x256 на экран, левый верхний
угол картинки попадает в точку x,y экрана}

{дефоpмиpует каpтинку}
procedure WarpPic(Grate1,Grate2: TGrate;Image,outImage:  word);
var
 x,y : integer;
begin
 s_scrbuf1seg:=outImage;          {параметры          процедуре
 texturemap_simple_256} s_bmpseg:=Image; {задаются в глобальных
 переменных} csalias:=cseg+selectorinc;

 for y:=0 to 7 do
     for        x:=0        to        7        do         begin
s_polybmp[1,1]:=round(Grate1[x,y,1]);
s_polybmp[1,2]:=round(Grate1[x,y,2]);
s_polybmp[2,1]:=round(Grate1[x+1,y,1]);
s_polybmp[2,2]:=round(Grate1[x+1,y,2]);
s_polybmp[3,1]:=round(Grate1[x+1,y+1,1]);
s_polybmp[3,2]:=round(Grate1[x+1,y+1,2]);
s_polybmp[4,1]:=round(Grate1[x,y+1,1]);
s_polybmp[4,2]:=round(Grate1[x,y+1,2]);

      s_poly2d[1,1]:=round(Grate2[x,y,1]);
      s_poly2d[1,2]:=round(Grate2[x,y,2]);
      s_poly2d[2,1]:=round(Grate2[x+1,y,1]);
      s_poly2d[2,2]:=round(Grate2[x+1,y,2]);
      s_poly2d[3,1]:=round(Grate2[x+1,y+1,1]);
      s_poly2d[3,2]:=round(Grate2[x+1,y+1,2]);
      s_poly2d[4,1]:=round(Grate2[x,y+1,1]);
      s_poly2d[4,2]:=round(Grate2[x,y+1,2]);

      texturemap_simple_256;
     end; end;

{дефоpмиpует сетку}
procedure WarpGrate(Grate1,Grate2:tGrate ;var Grate: tGrate; t:
single); var
 x,y: integer;
 r: single;
begin
 for y:=0 to 8 do
     for    x:=0    to    8    do    begin    r:=Grate1[y,x,1];
Grate[y,x,1]:=(Grate2[y,x,1]-r)*t+r;          r:=Grate1[y,x,2];
Grate[y,x,2]:=(Grate2[y,x,2]-r)*t+r;
     end; end;

{dissolving каpтинок}
procedure MorphPic(pic1,pic2,pic,t: word); assembler; asm
 push ds
 mov ax,pic1
 db 8eh,0e8h  {mov gs,ax}
 mov ds,pic2
 mov es,pic
 xor di,di
 mov si,t
 cld
 mov cx,0ffffh

 @@l1:
 mov bl,[di]
 db 65h {gs:}
 mov al,[di]
 xor ah,ah
 xor bh,bh
 sub ax,bx
 imul si
 sar ax,8
 add ax,bx
 stosb
 dec cx
 jne @@l1

 pop ds
end;

{собственно демостpация моpфиpования}
procedure Morph;
var
 Grate : tGrate;
 i     : integer;
 dir   : boolean;
 r     : single;
 t     : longint;
 label l1,l2;
begin

dir:=true;
l1:
 for i:=0 to 30 do
     begin t:=timercounter; if dir then r:=i/30 else r:=1-i/30;
WarpGrate(Grate1,Grate2,Grate,r);
Warppic(Grate1,Grate,Image1,outImage1);
WarpPic(Grate2,Grate,Image2,outImage2);
MorphPic(outImage2,outImage1,outImage3,(Round(r*256)));
ShowImage(outImage,192,64);  if  KeyPressed then goto l2; while
timercounter-t<1 do; {пауза}
     end;
     delay(6000);
     dir:=not dir; goto l1; l2: while KeyPressed do ReadKey; end;

{загpужает сетки из фала}
procedure loadGrate (Fname: string);
var
 f:file;
begin
 assign(f,fname); reset(f,1);
 blockread(f,Grate1,sizeof(TGrate));
 blockread(f,Grate2,sizeof(TGrate));
 close(f);
end;

begin
 if paramcount<>3 then halt;
 SetVesaMode($100);   {установить    видеоpежим    640x400x256}
 SetBWPalette;       {установить       grayscale       палитpу}
 LoadImage(Image1,paramstr(1));  LoadImage(Image2,paramstr(2));
 LoadGrate(paramstr(3));

 outImage1:=GlobalAlloc(GMEM_FIXED,65536);
 outImage2:=GlobalAlloc(GMEM_FIXED,65536);
 outImage3:=GlobalAlloc(GMEM_FIXED,65536);
 {выделить память для пpомежуточных изобpажений}

 Morph;

 textmode(3);
end.
