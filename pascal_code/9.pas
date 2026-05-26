program Test9;

type
  TIndex = integer;

const
  c, d = 5;
  e = 5.2;
  f = 'xdtest';
var
  a, b: integer;
  flag: boolean;

function add(x, y: integer): integer;
var
  result: integer;
begin
  result := x + y;
end;

procedure print(value: integer);
begin
  value := value + 1;
end;

begin
  a := 10;
  b := add(a, 20);
  flag := true;
end.