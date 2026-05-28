program Test13;

var
  n, result: integer;

function factorial(x: integer): integer;
begin
  if x = 1 then
    result := 1
  else
    result := x * factorial(x - 1);
end;

begin
  n := 5;
  result := factorial(n);
end.