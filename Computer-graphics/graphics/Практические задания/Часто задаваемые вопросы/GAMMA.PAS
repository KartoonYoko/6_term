uses Crt;

var  Scr: array[0..199,0..319] of Byte absolute $A000:$0000;

const Gamma:Real=1.8;

procedure SetPALColor(R,G,B:Real{0..1});
{α γη₯β®¬ £ ¬¬λ}
procedure Out1(V:Real);
begin
  if V<1E-3   then Port[$3C9]:=0
  else if V>1 then Port[$3C9]:=63
              else Port[$3C9]:=Round(63*Exp(Ln(V)/Gamma));
end; {Out1}

begin {SetPalColor}
  Out1(R);
  Out1(G);
  Out1(B);
end;  {SetPalColor}

procedure SetPalette;
var   N : Integer;
begin
  Port[$3C8] := 128;
  for N:=0 to 127 do
    SetPalColor(N/127,N/127,N/127);
end; {of SetPalette}

var   X,Y: Integer;
begin
  DirectVideo:=False;

  asm mov ax,$13; int $10; end;
  for Y:=0 to 39 do begin
    for X:=0 to 99 do begin
      Scr[20+Y*2,159-X]:=128;
      Scr[21+Y*2,159-X]:=254;
      Scr[20+Y*2,160+X]:=191;
      Scr[21+Y*2,160+X]:=191;
    end;
  end;
  for Y:=0 to 79 do begin
    for X:=0 to 49 do begin
      Scr[100+Y,159-X*2]:=191;
      Scr[100+Y,158-X*2]:=191;
      Scr[100+Y,161+X*2]:=128;
      Scr[100+Y,160+X*2]:=254;
    end;
  end;

  for Y:=0 to 79 do begin
    for X:=0 to 99 do begin
      Scr[60+Y,109+X]:=128+((X+Y) and 1)*126;
    end;
  end;

  for Y:=20 to 59 do begin
    for X:=25 to 74 do begin
      Scr[60+Y,109+X]:=191;
    end;
  end;

  Write('                       <+> <-> to adjust');
  repeat
    SetPalette;
    Write(#13'                 '#13,'Gamma = ',Gamma:1:3);
    case ReadKey of
      '+': Gamma:=Gamma*1.01;
      '-': Gamma:=Gamma/1.01;
      #27:Break;
    end;
  until False;
  asm mov ax,$03; int $10; end;
end.
