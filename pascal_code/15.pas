program RecordExample1;

type
  Address = record
    street  : string;
    city    : string;
    zipCode : integer;
  end;

  Employee = record
    id        : integer;
    name      : string;
    salary    : real;
    active    : boolean;
    home      : Address;
    scores    : array[1..5] of integer;
  end;

var
  emp : Employee;
  i   : integer;

begin
  emp.id := 1001;
  emp.name := 'Alice';
  emp.salary := 5200.50;
  emp.active := true;

  emp.home.street := 'Main Street';
  emp.home.city := 'Krakow';
  emp.home.zipCode := 30001;

  for i := 1 to 5 do
  begin
    emp.scores[i] := i * 10;
  end;
end.