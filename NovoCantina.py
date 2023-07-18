
#DICIONÁRIO

cardapio = {
    100: {
        "codigo": 100,
        "produto": "Cachorro quente",
        "preço": 9.00
    },
    101: {
        "codigo": 101,
        "produto": "Cachorro quente duplo",
        "preço": 11.00
    },
    102: {
        "codigo": 102,
        "produto": "X-Egg",
        "preço": 12.00
    },
    103: {
        "codigo": 103,
        "produto": "X- Salada",
        "preço": 13.00
    },
    104: {
        "codigo": 104,
        "produto": "x-Bacon",
        "preço": 14.00
    },
    105: {
        "codigo": 105,
        "produto": "X-Tudo",
        "preço": 17.00
    },
    200: {
        "codigo": 200,
        "produto": "Refrigerante lata",
        "preço": 9.00
    },
    201: {
        "codigo": 201,
        "produto": "Chá gelado",
        "preço": 4.00
    },
}


#IMPRESSÃO DO CARDÁPIO
print("       Bem-vindo a Lanchonete do SENAI")
print(" ***************** CARDÁPIO **************")

produto = ""
for i in cardapio:
    produto = cardapio[i]["produto"]
    while len(produto) != len(cardapio[101]["produto"])+2:
        produto = produto +" "

    print (f"| {cardapio[i]['codigo']}  | {produto} | R$  {cardapio[i]['preço']:.2f} |")


# PEDIDO

total = 0
estrato = []
precos = []

while True:
    codigo = int(input('Entre com o código desejado:  '))
    while codigo not in (cardapio):
        print("Código inválido!")
        codigo = int(input('Entre com o código desejado:  '))

    total = total + cardapio[codigo]["preço"]

    print (f"Você pediu um {cardapio [codigo]['produto']}, no valor de R$ {cardapio [codigo]['preço']:.2f} ")

    estrato.append(cardapio [codigo]["produto"])
    precos.append(cardapio[codigo]["preço"])

    adicional = input('Deseja pedir mais alguma coisa (Sim/Não):  ').lower()

    if adicional == "sim":
        continue
    else:
        if adicional == "não":
            break
        else:
            print("Opção Inválida")


#IMPRESSÃO DO EXTRATO 
print("\n***********EXTRATO DO PEDIDO**************")
for i in range(0, len(estrato),1):
    print (estrato[i], "-------------------- R$", precos[i])


print(f"TOTAL: R$ {total}")