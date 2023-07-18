
preco_unitario = float(input("Digite o preço unitário: ").replace(",","."))
quantidade = int(input("Digite a quantidade: ").replace(",","."))

total_sem_desconto = preco_unitario*quantidade

resultado = '{:.2f}'.format(total_sem_desconto).replace(".",",")
print ("Valor total sem desconto: R$",resultado)

if quantidade <= 9:
    print ("Não recebe desconto")
elif quantidade >=10 and quantidade<=99:
    total_desconto = '{:.2f}'.format(total_sem_desconto*(1-0.05))
    print ("Valor total com desconto: R$", total_desconto)
elif quantidade >=100 and quantidade<=999:
    total_desconto = '{:.2f}'.format(total_sem_desconto*(1-0.10))  
    print ("Valor total com desconto: R$", total_desconto)
else: 
    total_desconto = '{:.2f}'.format(total_sem_desconto*(1-0.15))
    print ("Valor total com desconto: R$", total_desconto)