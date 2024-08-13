grammar Policy;

/*
 * Parser Rules
 */

policy: statements* invariant statements* EOF;
statements: invariant | condition_assignment;
invariant : IF if_condition THEN then_condition;
if_condition : OPEN_PAREN? predicate  CLOSED_PAREN? |  OPEN_PAREN? predicate AND if_condition CLOSED_PAREN? | OPEN_PAREN? predicate OR if_condition CLOSED_PAREN? |  NOT OPEN_PAREN? if_condition CLOSED_PAREN?;
predicate : OPEN_PAREN? predicate_factor  CLOSED_PAREN? | OPEN_PAREN? predicate_factor AND predicate CLOSED_PAREN? | predicate_factor OR predicate CLOSED_PAREN? | NOT OPEN_PAREN? predicate CLOSED_PAREN?;
predicate_factor :  OPEN_PAREN? term RELATIONAL_OP term CLOSED_PAREN? | condition_assigned_variable | TRUE;
then_condition : OPEN_PAREN? if_condition CLOSED_PAREN? | OPEN_PAREN? if_condition SINCE then_condition CLOSED_PAREN? | YESTERDAY then_condition | NOT OPEN_PAREN? then_condition CLOSED_PAREN?;

term: term_factor | term ARITHMATIC_OP term_factor;
term_factor : condition_assigned_variable | device '.' device_attribute | constant | function_call;
function_call: function OPEN_PAREN terms CLOSED_PAREN;
terms : term_factor? | term_factor COMMA terms;
constant : TIME | INTEGER | REAL_NUMBER | STRING;
function : IDENTIFIER;
device : IDENTIFIER;
device_attribute: IDENTIFIER;
condition_assigned_variable: IDENTIFIER;

condition_assignment: condition_assigned_variable '=' OPEN_PAREN? (predicate | constant | function_call) CLOSED_PAREN?;


/*
 * Lexer Rules
 */

fragment LETTER  : [a-zA-Z] ;
fragment DIGIT      : [0-9] ;
fragment UNDERSCORE : '_';

/* relational operators */
fragment EQ         :   '==';
fragment NE         :   '!=';
fragment GE         :   '>=';
fragment LE         :   '<=';
fragment GT         :   '>';
fragment LT         :   '<';

/* keywords */
IF : 'If';
THEN : 'Then';
AND: 'and';
OR: 'or';
NOT: 'not';
TRUE: 'true';
SINCE: 'since';
YESTERDAY: 'yesterday';

INTEGER             : [+-]?DIGIT+;
REAL_NUMBER         : [+-]?DIGIT+ ('.' DIGIT+)?;
STRING              : '"'(LETTER|DIGIT|UNDERSCORE)+ '"';
TIME                : HOUR (':' MINUTE ( ':' SECOND )?)? ('am'|'pm')?;
HOUR                : DIGIT DIGIT?;
MINUTE              : DIGIT DIGIT;
SECOND              : DIGIT DIGIT;
IDENTIFIER          : LETTER (LETTER|DIGIT|UNDERSCORE)*;
RELATIONAL_OP       : EQ | NE | GE | LE | GT | LT;
ARITHMATIC_OP       : '+' | '-' | '*' | '/';
OPEN_PAREN : '(';
CLOSED_PAREN: ')';
COMMA: ',';

WHITESPACE          : (' ' | '\t')+ ->skip ;
NEWLINE             : ('\r'? '\n' | '\r')+ ->skip ;
COMMENTS            : '#' ~[\r\n]+ -> skip;
