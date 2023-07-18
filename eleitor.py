
idade = int(input("Digite a idade: "))


if (idade >= 16  and idade <18) or (idade>70):
    print("Voto opcional")
elif idade >=18 and idade <=70:
    print ("voto obrigatório")
else:
    print ("Não vota")



'''''
Opção sem construir uma lógica para os opcionais
if idade < 16:
    print("não vota")
elif idade >=18 and idade <=70:
    print ("voto obrigatório")
else:
    print ("Voto opcional")
'''''

