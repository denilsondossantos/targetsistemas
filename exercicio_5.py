'''5) Escreva um programa que inverta os caracteres de um string.


IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;
'''

lista = list(input(('Digite uma string: ')))

string_reversa = ""

for i in range(len(lista), 0, -1):
    string_reversa += lista[i-1]

print(str(string_reversa))