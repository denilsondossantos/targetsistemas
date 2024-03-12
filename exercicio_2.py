''''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será 
a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
escreva um programa na linguagem que desejar onde, informado um número, 
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado 
pertence ou não a sequência.



IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou 
pode ser previamente definido no código;

'''
n1= 1
n2=1
lista = [0,1,1]
entrada = int(input('\nDigite um número: '))

for i in range(0, (entrada*2)):
    x = n1 + n2
    lista.append(x)
    n2 = x
    n1 = (x-n1)


if entrada in lista:
    print('\nPertence')
else:
    print('\nNão pertence')

