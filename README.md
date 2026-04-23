# Konwerter PASCAL do C
Projekt konwertera progrmów w języku Pascal do języka C

- Autor:
    - Szymon Konieczny: skonieczny@student.agh.edu.pl

- Założenia programu:
    - konwerter
    - planowany język implementacji: python
    - wejście: poprawny program w języku Pascal
    - wyjście: program przekonwertowany na program w języku C
    - generator parserów: ANTLR

 - Gramatyka jest w pliku pascal.g4
 - Spis tokenów rozpoznawanych przez lexer:

| Token             | Wzorzec                 | Opis |
|------------------|-----------------------------------|------|
| KW_AND           | `'and'`                           | operator logiczny AND |
| KW_ARRAY         | `'array'`                         | deklaracja tablicy |
| KW_BEGIN         | `'begin'`                         | początek bloku |
| KW_CASE          | `'case'`                          | instrukcja case |
| KW_CONST         | `'const'`                         | deklaracja stałych |
| KW_DIV           | `'div'`                           | dzielenie całkowite |
| KW_DO            | `'do'`                            | część pętli |
| KW_DOWNTO        | `'downto'`                        | pętla malejąca |
| KW_ELSE          | `'else'`                          | gałąź alternatywna |
| KW_END           | `'end'`                           | koniec bloku |
| KW_FOR           | `'for'`                           | pętla for |
| KW_FUNCTION      | `'function'`                      | deklaracja funkcji |
| KW_IF            | `'if'`                            | instrukcja warunkowa |
| KW_IN            | `'in'`                            | operator in (niewykorzystany) |
| KW_MOD           | `'mod'`                           | modulo |
| KW_NIL           | `'nil'`                           | wartość pusta |
| KW_NOT           | `'not'`                           | negacja |
| KW_OF            | `'of'`                            | część deklaracji |
| KW_OR            | `'or'`                            | operator logiczny OR |
| KW_PROCEDURE     | `'procedure'`                     | deklaracja procedury |
| KW_PROGRAM       | `'program'`                       | nagłówek programu |
| KW_REPEAT        | `'repeat'`                        | pętla repeat |
| KW_SET           | `'set'`                           | zbiór (niewykorzystany) |
| KW_THEN          | `'then'`                          | część if |
| KW_TO            | `'to'`                            | pętla rosnąca |
| KW_TYPE          | `'type'`                          | deklaracja typów |
| KW_UNTIL         | `'until'`                         | warunek zakończenia |
| KW_VAR           | `'var'`                           | deklaracja zmiennych |
| KW_WHILE         | `'while'`                         | pętla while |
| KW_INTEGER       | `'integer'`                       | typ całkowity |
| KW_REAL          | `'real'`                          | typ rzeczywisty |
| KW_BOOLEAN       | `'boolean'`                       | typ logiczny |
| KW_STRING        | `'string'`                        | typ tekstowy |
| LOGIC_LITERAL    | `'true' \| 'false'`               | wartości logiczne |
| LT               | `'<'`                             | mniejsze niż |
| GT               | `'>'`                             | większe niż |
| LE               | `'<='`                            | mniejsze lub równe |
| GE               | `'>='`                            | większe lub równe |
| EQ               | `'='`                             | równość |
| NE               | `'<'>'`                           | nierówność |
| ASSIGN           | `':='`                            | przypisanie |
| DOT              | `'.'`                             | koniec programu |
| ARRAY_INDEX_TYPE | `'-'?[0-9]+ ('..' '-'?[0-9]+)?`   | zakres indeksów tablicy |
| NUMBER           | `[0-9]+('.'[0-9]+)?`              | liczba całkowita / rzeczywista |
| STRING           | `'\'' ( '\'\'' \| ~'\'' )* '\''`  | literał tekstowy |
| IDENTIFIER       | `[a-zA-Z_][a-zA-Z_0-9]*`          | identyfikator |
| WS               | `[ \t\r\n]+`                      | białe znaki |
| COMMENT          | `'(*' .*? '*)'`                  | komentarz blokowy |
| LINE_COMMENT     | `'//' ~[\r\n]*`                   | komentarz liniowy |