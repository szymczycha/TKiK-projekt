program Test10;

var
  i, sum: integer;

begin
  i := 1;
  sum := 0;

  while i <= 10 do
    begin
      if i mod 2 = 0 then
        sum := sum + i
      else
        sum := sum - i;

      i := i + 1;
    end;
end.