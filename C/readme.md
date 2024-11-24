bison -d matemagica.y
flex matemagica.l
gcc -o matemagica matemagica.tab.c lex.yy.c -lfl
./matemagica < entrada.
