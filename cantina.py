
cardapio =  { 100: "cachorro quente", 101: "cachorro quente duplo", 102: "X-egg", 103: "x-salada", 104: "x-bacon", 105: "x-tudo", 200: "refrigerante lata" , 201: "chá gelado"}

valores =  {100: 9.00, 101: 11.00, 102: 12.00, 103: 13.00, 104: 14.00, 105: 17.00, 200: 9.00, 201: 4.00,}


print("       Bem-vindo a Lanchonete do SENAI")
print(" ***************** CARDÁPIO ****************")
print(" | Código |        Descrição        | Valor |")
print(" |   100  |     Cachoorro Quente    |  9,00 |")
print(" |   101  |  Cachoorro Quente Duplo | 11,00 |")
print(" |   102  |         X - Egg         | 12,00 |")
print(" |   103  |        X - Salada       | 12,00 |")
print(" |   104  |         X -Bacon        | 14,00 |")
print(" |   105  |         X -Tudo         | 17,00 |")
print(" |   200  |     Refrigerante Lata   |  5,00 |")
print(" |   201  |        Chá Gelado       |  4,00 |")

total = 0

while True:
    codigo = int(input('Entre com o código desejado:  '))
    while codigo not in (cardapio):
        print("Código inválido!")
        codigo = int(input('Entre com o código desejado:  '))

    prod = cardapio [codigo]
    preco = valores[codigo]
    total = total + preco

    print (f"Você pediu um {prod} no valor de {preco}")

    adicional = input('Deseja pedir mais alguma coisa (Sim/Não):  ').lower()

    if adicional == "sim":
        continue
    else:
        if adicional == "não":
            break
        else:
            print("Opção Inválida")

print(f"O total a ser pago é: {total}")
