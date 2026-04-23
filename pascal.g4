grammar pascal;

program : program_header block DOT;
program_header : KW_PROGRAM IDENTIFIER ('('('input')? (','? 'output')?')')? ';' ;

declarations : type_declarations? const_declarations? var_declarations? func_and_proc_declarations? ;

type_declarations : KW_TYPE (type_decl | array_decl)+;
type_decl : IDENTIFIER '=' type_spec ';';
array_decl: IDENTIFIER '=' KW_ARRAY '[' ARRAY_INDEX_TYPE (',' ARRAY_INDEX_TYPE)* ']' KW_OF type_spec ';' ;

const_declarations : KW_CONST const_decl+;
const_decl : IDENTIFIER (',' IDENTIFIER)* '=' literal ';';

var_declarations : KW_VAR var_decl+ ;
var_decl : IDENTIFIER (',' IDENTIFIER)* ':' type_spec ';' ;
type_spec : KW_INTEGER
    | KW_REAL
    | KW_BOOLEAN
    | KW_STRING
    ;

func_and_proc_declarations : (func_declaration | proc_declaration)+ ;
func_declaration : KW_FUNCTION IDENTIFIER func_arguments? ':' type_spec ';' block ';';
func_arguments : '(' func_argument_grp (';' func_argument_grp)* ')' ;
func_argument_grp :  KW_VAR? IDENTIFIER (',' IDENTIFIER)* ':' type_spec ;

proc_declaration : KW_PROCEDURE IDENTIFIER func_arguments? ';' block ';';


block : declarations KW_BEGIN statement_list? KW_END;

code_block : KW_BEGIN statement_list? KW_END;
statement_list : statement (';' statement)* ';'? ;

statement : code_block 
    | function_call 
    | assignment
    | if_block
    | for_loop
    | repeat_loop
    | while_loop
    | case_statement
    ;

case_statement : KW_CASE expression KW_OF (case_branch ';'?)* (KW_ELSE statement ';'?)? KW_END;
case_branch : case_label (',' case_label)* ':' statement;
case_label : NUMBER
    | STRING
    | IDENTIFIER
    ;

for_loop : KW_FOR IDENTIFIER ASSIGN expression (KW_TO | KW_DOWNTO) expression KW_DO statement;

repeat_loop : KW_REPEAT statement_list KW_UNTIL expression;

if_block : KW_IF expression KW_THEN statement (KW_ELSE statement)?;

while_loop : KW_WHILE expression KW_DO statement;

function_call : IDENTIFIER '(' arg_list? ')';
arg_list : expression (',' expression)* ;

expression : orExpr ;
orExpr : andExpr (KW_OR andExpr)* ;
andExpr : relation (KW_AND relation)* ;
relation : addition ((EQ | NE | LT | LE | GT | GE) addition)* ;
addition : term (('+' | '-') term)* ;
term : factor (('*' | '/' | KW_DIV | KW_MOD) factor)* ;
factor : ('+'|'-'|KW_NOT) factor 
    | literal
    | function_call
    | IDENTIFIER
    | '(' expression ')'
    ;

assignment : IDENTIFIER ASSIGN expression;

literal : NUMBER | STRING | LOGIC_LITERAL | KW_NIL;


KW_AND        : 'and' ;
KW_ARRAY      : 'array' ;
KW_BEGIN      : 'begin' ;
KW_CASE       : 'case' ;
KW_CONST      : 'const' ;
KW_DIV        : 'div' ;
KW_DO         : 'do' ;
KW_DOWNTO     : 'downto' ;
KW_ELSE       : 'else' ;
KW_END        : 'end' ;
KW_FOR        : 'for' ;
KW_FUNCTION   : 'function' ;
KW_IF         : 'if' ;
KW_IN         : 'in' ;
KW_MOD        : 'mod' ;
KW_NIL        : 'nil' ;
KW_NOT        : 'not' ;
KW_OF         : 'of' ;
KW_OR         : 'or' ;
KW_PROCEDURE  : 'procedure' ;
KW_PROGRAM    : 'program' ;
KW_REPEAT     : 'repeat' ;
KW_SET        : 'set' ;
KW_THEN       : 'then' ;
KW_TO         : 'to' ;
KW_TYPE       : 'type' ;
KW_UNTIL      : 'until' ;
KW_VAR        : 'var' ;
KW_WHILE      : 'while' ;


KW_INTEGER : 'integer';
KW_REAL    : 'real';
KW_BOOLEAN : 'boolean';
KW_STRING  : 'string';


LOGIC_LITERAL : 'true' | 'false';

// L_PAREN    : '(';
// R_PAREN    : ')';
// L_BRACKET  : '[';
// R_BRACKET  : ']';
// L_BRACE    : '{';
// R_BRACE    : '}';

LT : '<';
GT : '>';
LE : '<=';
GE : '>=';
EQ : '=';
NE : '<>';

ASSIGN     : ':=';
DOT        : '.';

ARRAY_INDEX_TYPE: '-'?[0-9]+ ('..''-'?[0-9]+)?; // used in array declaration
NUMBER     : [0-9]+('.' [0-9]+)? ;
STRING     : '\'' ( '\'\'' | ~'\'' )* '\'' ;

WS         : [ \t\r\n]+ -> skip ;
COMMENT    : '(*' .*? '*)' -> skip ;
LINE_COMMENT : '//' ~[\r\n]* -> skip ;
IDENTIFIER : [a-zA-Z_][a-zA-Z_0-9]* ;
