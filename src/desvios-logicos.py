idade = 17;

# isso so recebe valores boolean so vai imprimir se o valor for verdadeiro(True)
if idade < 18:
    print(f'voce e menor ds idade { idade }');


# na empresao acima podemos ver que se o valor idade for maior ou ingual a 18 nao imprime nada na tela
#podemos mudar isso com o else:
idade2 = 19;

if idade2 < 18:
    print(f'voce e menor ds idade { idade2 }');
else:
    print(f'voce e maior de idade { idade2 }');


idade3 = 19;

if idade3 < 18:
    print(f'voce e menor ds idade { idade3 }');

else if idade3 >= 60:
    print(f'voce e idosa: { idade3 }');

else:
    print(f'voce e maior de idade { idade3 }');
