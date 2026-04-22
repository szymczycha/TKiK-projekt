program Test11;

var
  i, j, total: integer;

begin
  total := 0;

  for i := 1 to 5 do
    total := total + i * 2;

  j := 0;
  repeat
    j := j + 1;
    total := total + j;
  until j = 5;
end.