program ArrayExample;

type
  IntArray = array[1..5] of integer;

var
  numbers : IntArray;
  i       : integer;
  total   : integer;

begin
  { Assign values using numeric indexes }
  numbers[1] := 10;
  numbers[2] := 20;
  numbers[3] := 30;
  numbers[4] := 40;
  numbers[5] := 50;

  total := 0;

  { Read values using numeric indexes }
  for i := 1 to 5 do
  begin
    total := total + numbers[i];
  end;

  numbers[3] := numbers[1] + numbers[2];

  total := 0;

  for i := 1 to 5 do
  begin
    total := total + numbers[i];
  end;
end.