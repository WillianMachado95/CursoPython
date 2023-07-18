
disciplinas = int(input('Quantas disciplinas deseja cadastrar?  '))

for disciplina in range (1,disciplinas+1,1):

    nome_disciplina = (input(f'Informe o nome da Disciplina {disciplina}:  '))
    avaliacao = int(input('Quantas notas deseja informar para esta disciplina?  '))
    media = 0

    for i in range (1,avaliacao+1,1):
        nota = float(input(f'Qual a nota {i}? ').replace(",","."))
        media = media + nota 
        mediaf = media/avaliacao
        
    print (f"A média do aluno é:  {mediaf:.2}")





