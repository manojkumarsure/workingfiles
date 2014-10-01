
%{
#include<stdio.h>
#include<stdlib.h>
#include "P1.tab.h"
%}
%x comment1
%x comment2
%%
[ \n\t] ;
<<EOF>> return e0f;
abfg return e0f;
"/*" BEGIN(comment1);
<comment1>[^*\n]* ;
<comment1>"*"+[^*/\n]* ;
<comment1>\n ;
<comment1>"*"+"/" BEGIN(INITIAL);
"//" BEGIN(comment2);
<comment2>[^\n]* ;
<comment2>\n BEGIN(INITIAL);
class return CLASS;
public return PUBLIC;
static return STATIC;
void return VOID;
main return MAIN;
System.out.println return PRINT;
extends return EXTEND;
return return RETURN;
int return INT;
boolean return BOOL;
if return IF;
else return ELSE;
while return WHILE;
length return LENGTH;
true { yylval.boolval= strdup(yytext); return TRUE;}
false { yylval.boolval= strdup(yytext); return FALSE;}
this return THIS;
new return NEW;
#define return DEFINE;
String return STRING;
[a-zA-Z_][a-zA-Z0-9_]* {yylval.identifier=strdup(yytext); return IDENTIFIER;}
[1-9][0-9]*|0 {yylval.integer=atoi(yytext); return INTEGER;}
[;\,\{\}\(\)\[\]\.] { return yytext[0]; }
[\+\*\/\%\^\!\=\<\>\&\-] { yylval.op_value=strdup(yytext); return yylval.op_value[0]; }
. ;
%%
