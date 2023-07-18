
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



print("       Bem-vindo a Lanchonete do SENAI")
print(" ***************** CARDÁPIO **************")

produto = "x"
for i in cardapio:
    produto = cardapio[i]["produto"]
    while len(produto) != len(cardapio[101]["produto"])+2:
        produto = produto +" "
    print ("| ",cardapio[i]["codigo"]," |",produto,"| R$", cardapio[i]["preço"], "|")



