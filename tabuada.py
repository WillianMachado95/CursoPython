
#tabuada = int(input('Escolha o número da tabuada: '))

for tabuada in range (1,11,1):
    print (f" \nTABUADA DO {tabuada} \n************")
    for i in range (1,11,1):
        mult = tabuada * i
        print (f"{tabuada} x {i} = {mult}")