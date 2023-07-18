
avaliacao = int(input('Quantas notas deseja informar?  '))

soma = 0
for i in range (1,avaliacao+1,1):
   nota = float(input(f'Qual a nota {i}? ').replace(",","."))
   soma = soma + nota 

media = soma/avaliacao

print (f"A média do aluno é:  {media:.1f}")