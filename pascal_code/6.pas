program Test6;
begin
  x := 2;

  case x of
    1: y := 10;
    2: y := 20;
    3, 4: y := 30;
  else
    y := 0;
  end;
end.