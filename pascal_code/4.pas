program Test4;
begin
  sum := 0;

  for i := 1 to 5 do
    sum := sum + i;

  for j := 10 downto 1 do
    sum := sum + j;
end.