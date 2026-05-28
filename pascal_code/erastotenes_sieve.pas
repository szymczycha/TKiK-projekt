program EratosthenesSieve;

var
  isPrime: array[2..100] of boolean;
  i, j: integer;

begin
  for i := 2 to 100 do
    isPrime[i] := true;

  for i := 2 to trunc(sqrt(100)) do
  begin
    if isPrime[i] then
    begin
      j := i * i;
      while j <= 100 do
      begin
        isPrime[j] := false;
        j := j + i;
      end;
    end;
  end;

  writeln('Prime numbers up to 100:');
  for i := 2 to 100 do
  begin
    if isPrime[i] then
      writeln(i, ' ');
  end;

end.