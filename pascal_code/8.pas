program Test8;

begin
  a := 1;
  b := 2;
  c := 3;

  if a < b then
    begin
      c := c + 1;
      a := a + b;
    end
  else
    c := c - 1;

  for i := 1 to 3 do
    c := c + i;

  while c < 20 do
    c := c + 2;

  repeat
    c := c - 1;
  until c = 10;

  case c of
    10: a := 100;
    20: a := 200;
  else
    a := 0;
  end;

  result := max(a, c);
end.