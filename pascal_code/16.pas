program RecordExample2;

type
  DateRec = record
    day   : integer;
    month : integer;
    year  : integer;
  end;

  Book = record
    title       : string;
    author      : string;
    publishDate : DateRec;
    ratings      : array[1..3] of real;
  end;

  Library = record
    name  : string;
    books : array[1..2] of Book;
  end;

var
  lib : Library;

begin
  lib.name := 'Central Library';

  lib.books[1].title := 'Compiler Design';
  lib.books[1].author := 'John Smith';
  lib.books[1].publishDate.day := 15;
  lib.books[1].publishDate.month := 3;
  lib.books[1].publishDate.year := 2020;

  lib.books[1].ratings[1] := 4.5;
  lib.books[1].ratings[2] := 4.8;
  lib.books[1].ratings[3] := 5.0;

  lib.books[2].title := 'Algorithms';
  lib.books[2].author := 'Jane Doe';
  lib.books[2].publishDate.day := 1;
  lib.books[2].publishDate.month := 7;
  lib.books[2].publishDate.year := 2018;
end.