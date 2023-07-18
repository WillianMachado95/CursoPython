
avaliacao = int(input('Quantas notas deseja informar?  '))

soma = 0
somapesos = 0
for i in range (1,avaliacao+1,1):
   nota = float(input(f'Qual a nota {i}? ').replace(",","."))
   peso = float(input(f'Qual o peso da nota {i}?  ').replace(",","."))
  
   soma = soma + nota * peso
   somapesos = somapesos + peso

   media = soma/somapesos

print (f"A média do aluno é:  {media:.1f}")