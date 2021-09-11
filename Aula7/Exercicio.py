"""

* Cirar variáveis para nome(str), idade(int, altura(float) e peso(float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o ano de nascimento da pessoa (basedo na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da oessoa)
* Exibir um texto com todos os valores na tela usando F-strings (com as chaves)

"""

nome = 'claudiana'
idade = 21
altura = 1.65
peso = 88.900
ano_atual = 2021
ano_nascimento = ano_atual - (idade+1)  #nasci no final de dezembro. Deu fail aqui #sad
imc = peso/(altura**2)

print (f'O meu nome é {nome}, tenho {idade} anos de idade, nasci no final do ano de {ano_nascimento}. Meu peso é {peso}, altura {altura:.2f} e meu imc é igual a  {imc:.2f}')
