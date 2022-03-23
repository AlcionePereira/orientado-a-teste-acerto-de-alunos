'''9) Dada uma lista X numérica contendo 5 elementos, fazer um programa que crie e exiba na tela
uma lista Y. A lista Y deverá conter o mesmo conteúdo da lista X na ordem inversa.'''
from random import randint

max_lista = 5
listax = list(range(max_lista))
listay = list()


#lista y recebe lista x inversa
for i in range(max_lista):
    listax[i] = randint(0, 100)
    listay = listax[::-1]
print(listax)
print(listay)

