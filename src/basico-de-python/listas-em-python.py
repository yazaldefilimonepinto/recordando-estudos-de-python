istoEUmaLista = [];

print(type(istoEUmaLista));#isto vai retornar o tipo list

#podemos adicionar valores na lista.

istoEUmaListaDeNumerosInteiros = [1, 7, 3, 8, 9, 0]; #uma lista de numeros inteiros


print(istoEUmaListaDeNumerosInteiros);

#Numa lista podemos armazenar elementos de qualquer tipo.

umaListaQualquer = ['ola', 17, 1.7888, True, []];


print(len(umaListaQualquer));# isto retorna a quantidade de intem da lista


#para acessar algum elemento da lista.
print(umaListaQualquer[0]); # ola porque o python inicia a contagem do 0 nao do 1.


print(umaListaQualquer[-1])#[] que e o ultimo elemento da lista 
#e passar um numero negativi ele pega de tras pra frente.


#podemos acessar uma fatia da lista .

print(umaListaQualquer[0:3])# vai retornar todos os elementos da posicao 0 ate 2 menos o 3 .

listaComRange = list(range(1, 18)); # a funcao range retorna numeros aleatorios

print(listaComRange);# vai retornar uma lista de 1 a 17 menos o 18
