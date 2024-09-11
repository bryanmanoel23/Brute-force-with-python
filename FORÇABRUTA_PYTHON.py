import string
from itertools import combinations_with_replacement
from random import random,choice
##gera senha forte

valores = string.ascii_letters + string.punctuation + string.digits
tamanho = 1
senha = ""

print(valores)
for i in range(tamanho):
    senha += choice(valores)
print(senha)

##retorna as combinações possíveis 
def gerar_senha(length, value):
    comb = combinations_with_replacement(length, value)
    print(list(comb))

value = 'abc'

gerar_senha(value, 5)


