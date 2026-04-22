program Test12;

var
  x, y: integer;

begin
  x := 2;

  case x of
    1: y := 10;
    2, 3: y := 20;
    4: begin
         y := 40;
         y := y + 1;
       end;
  else
    y := 0;
  end;

  y := y + (x * 10) - 3;
end.