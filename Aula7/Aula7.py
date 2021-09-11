"""

Exibir valores formatados usando print(f'texto {variavel}'

"""

nome = 'claudiana'  # str
idade = 21  # int
altura = 1.65 # float
e_maior = idade > 18 # bool
peso = 86
imc = peso/(altura**2)

print('Nome: ', nome)
print('Idade: ', idade)
print('Altura: ', altura)
print('Idade é maior que 18? ', e_maior)
print('o imc é: ', imc)


print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
