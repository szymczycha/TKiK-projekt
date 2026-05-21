program SumaTablicy;

var
    liczby: array[1..5] of integer;
    i, suma: integer;

begin
    suma := 0;

    writeln('Podaj 5 liczb:');

    for i := 1 to 5 do
    begin
        readln(liczby[i]);
        suma := suma + liczby[i];
    end;

    writeln('Wprowadzone liczby:');

    for i := 1 to 5 do
    begin
        writeln('Liczba ', i, ': ', liczby[i]);
    end;

    writeln('Suma wszystkich liczb = ', suma);
end.