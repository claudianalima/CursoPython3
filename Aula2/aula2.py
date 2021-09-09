#print(123456)
#print('Claudiana', 'Lima')

print ('Claudiana', 'Lima', sep= '-')  # parâmetro sep está adicionando um '-' entre o espaço
print ('Claudiana', 'Lima', sep= '-', end='  ')  # 'end' adiocionará o '##' no final do segunda palavra

"""
exercicio aula 2

Adicionar pontuação no CPF fictício 182.487.250-06
"""

#minha tentativa

print('182', '487', '250', sep='.', end='')
print('', '06', sep='-')

#solucção do professor

print('182', '487', '250', sep='.', end='-')
print('06', end= ' ')

print('Estou', 'aprendendo', 'Python', sep='-', end=' ')
print('isso é muito', 'legal', sep='-', end='')