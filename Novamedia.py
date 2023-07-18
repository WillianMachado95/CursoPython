
avaliacao = int(input('Quantas notas deseja informar?  '))

notas = []
for i in range (1,avaliacao+1,1):
   nota = float(input(f'Qual a nota {i}? ').replace(",","."))
   notas.append(nota)

media = sum(notas)/avaliacao


print (str(f"A média para as notas {notas} é:  {media:.1f}").replace("[", "").replace("]",""))
