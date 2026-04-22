program Test13;

var
  n, result: integer;

function factorial(x: integer): integer;
begin
  if x = 1 then
    factorial := 1
  else
    factorial := x * factorial(x - 1);
end;

procedure inc(var x: integer);
begin
  x := x + 1;
end;

begin
  n := 5;
  inc(n);
  result := factorial(n);
end.