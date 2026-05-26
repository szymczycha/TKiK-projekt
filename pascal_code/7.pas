program Test7;
var
  a, b, c : integer;
begin
  a := max(10, 20);
  b := min(a, 5 + 3 * 2);
  c := max(a, min(b, 100));
end.