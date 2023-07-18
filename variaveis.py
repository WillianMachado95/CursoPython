
'''
nome = input("Digite o seu nome: ")
print ("Olá, ",nome,"!")
print(f"Olá, {nome}!")

'''

num1 = float(input("Digite um número: ").replace(",","."))
num2 = float(input("Digite mais um número: ").replace(",","."))

soma = num1+num2

print("soma = ", soma)
print(str("soma= ",soma).replace(".",","))
