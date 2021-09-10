"""
Operadores Aritméticos

+ - adição
- - subtração
* - multiplicação
/ - divisão
// - divisão de inteiros
** - potenciação
% - módulo/resto da divisão
() - alterar a precedência nas contas


( n + n ) - Os parênteses têm a maior precedência, contas dentro deles são realizadas primeiro

** - Depois vem a exponenciação

* / //  % - Na sequência multiplicação, divisão, divisão inteira e módulo

+  - - Por fim, soma e subtração

Contas com operadores de mesma precedência são realizadas da esquerda para a direita.

"""
a = 10
b = 15
c = 2
print('adição', a+b)
print('divisão', a-c)
print('multiplicação', a*a)
print('divisão', a/c)
print('divisão inteira', b//c)
print('pontenciação', a**c)
print('módulo', a % b)
print('precedência de (a * b) + c =', a*(b+c), '\nmultiplicação de a * b + c = ', a*b+c)

"""
A função print() permite que um valor inteiro assuma a função de repetição de uma cadeia de caracteres
"""

print(10 * 'teste ', '\nA palavra "teste" foi repetida 10 vezes.')
