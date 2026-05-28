# Kompilator PASCAL do C
Projekt kompilatora progrmów w języku Pascal do języka C

- Autor:
    - Szymon Konieczny: skonieczny@student.agh.edu.pl

- Założenia programu:
    - kompilator
    - wejście: poprawny program w języku Pascal
    - wyjście: program przekonwertowany na program w języku C
    - język implementacji: python
    - generator parserów: ANTLR4

 - Gramatyka jest w pliku [pascal.g4](https://github.com/szymczycha/TKiK-projekt/blob/main/pascal.g4)
 - Spis tokenów rozpoznawanych przez lexer:

| Token             | Wzorzec                                   | Opis |
|------------------|--------------------------------------------|------|
| KW_AND           | `'and'`                                    | operator logiczny AND |
| KW_ARRAY         | `'array'`                                  | deklaracja tablicy |
| KW_BEGIN         | `'begin'`                                  | początek bloku kodu |
| KW_CASE          | `'case'`                                   | instrukcja wyboru |
| KW_CONST         | `'const'`                                  | deklaracja stałych |
| KW_DIV           | `'div'`                                    | dzielenie całkowite |
| KW_DO            | `'do'`                                     | część pętli |
| KW_DOWNTO        | `'downto'`                                 | iteracja malejąca |
| KW_ELSE          | `'else'`                                   | alternatywna gałąź |
| KW_END           | `'end'`                                    | koniec bloku |
| KW_FOR           | `'for'`                                    | pętla for |
| KW_FUNCTION      | `'function'`                               | deklaracja funkcji |
| KW_IF            | `'if'`                                     | instrukcja warunkowa |
| KW_IN            | `'in'`                                     | operator `in` |
| KW_MOD           | `'mod'`                                    | modulo |
| KW_NIL           | `'nil'`                                    | wartość pusta |
| KW_NOT           | `'not'`                                    | negacja logiczna |
| KW_OF            | `'of'`                                     | część deklaracji typu/tablicy |
| KW_OR            | `'or'`                                     | operator logiczny OR |
| KW_PROCEDURE     | `'procedure'`                              | deklaracja procedury |
| KW_PROGRAM       | `'program'`                                | nagłówek programu |
| KW_RECORD        | `'record'`                                 | deklaracja rekordu |
| KW_REPEAT        | `'repeat'`                                 | początek pętli repeat |
| KW_THEN          | `'then'`                                   | część instrukcji if |
| KW_TO            | `'to'`                                     | iteracja rosnąca |
| KW_TYPE          | `'type'`                                   | deklaracja typów |
| KW_UNTIL         | `'until'`                                  | warunek zakończenia repeat |
| KW_VAR           | `'var'`                                    | deklaracja zmiennych |
| KW_WHILE         | `'while'`                                  | pętla while |
| KW_INTEGER       | `'integer'`                                | typ całkowity |
| KW_REAL          | `'real'`                                   | typ rzeczywisty |
| KW_BOOLEAN       | `'boolean'`                                | typ logiczny |
| KW_STRING        | `'string'`                                 | typ tekstowy |
| LOGIC_LITERAL    | `'true' \| 'false'`                        | literał logiczny |
| LT               | `'<'`                                      | operator mniejszości |
| GT               | `'>'`                                      | operator większości |
| LE               | `'<='`                                     | operator mniejsze lub równe |
| GE               | `'>='`                                     | operator większe lub równe |
| EQ               | `'='`                                      | operator równości |
| NE               | `'<>'`                                     | operator nierówności |
| ASSIGN           | `':='`                                     | przypisanie |
| DOT              | `'.'`                                      | zakończenie programu / dostęp do pól |
| NUMBER           | `[0-9]+('.'[0-9]+)?`                       | liczba całkowita lub rzeczywista |
| STRING           | `'\'' ( '\'\'' \| ~'\'' )* '\''`           | literał tekstowy |
| IDENTIFIER       | `[a-zA-Z_][a-zA-Z_0-9]*`                   | identyfikator |
| WS               | `[ \t\r\n]+ -> skip`                       | białe znaki |
| COMMENT          | `'(*' .*? '*)' -> skip`                    | komentarz Pascalowy |
| OTHER_COMMENT    | `'{' .*? '}' -> skip`                      | komentarz w nawiasach klamrowych |
| LINE_COMMENT     | `'//' ~[\r\n]* -> skip`                    | komentarz jednoliniowy |

### Przykład użycia
Najprostszy przykład kompilacji plików:
```bash
python patocc.py kod_w_pascalu1.pas kod_w_pascalu2.pas kod_w_pascalu3.pas
```
Przykład kompilacji folderu plików w Pascalu z plikami wynikowymi:
```bash
python patocc.py .\patocc.py -d .\pascal_code\ -o .\compiled_pascal_to_c\
```

Przykładowy plik w Pascalu:
```pascal
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
```
Przekompilowany do C:
```c
#include <stdio.h>
#include <math.h>
#include <stdbool.h>
bool isPrime[100];
int i;
int j;
int main(){
    for(int i = 2; i <= 100; i++)isPrime[i]=true;
    
    for(int i = 2; i <= trunc(sqrt(100)); i++){
        if(isPrime[i]){
            j=i*i;
            while(j<=100){
                isPrime[j]=false;
                j=j+i;
            }
            
        }
        
    }
    
    printf("Prime numbers up to 100:\n");
    for(int i = 2; i <= 100; i++){
        if(isPrime[i])printf("%i \n", i);
        
    }
    
}
```
