
ca = float(input("Digite o valor do cateto A: ").replace(",","."))
cb = float(input("Digite o valor do cateto B: ").replace(",","."))

ca2 = ca**2
cb2 = cb**2
h = (ca2 + cb2)**0.5

perimetro = ca+cb+h
print ("O perímetro do triângulo retângulo é: ",perimetro)

area = (ca*cb)/2
print ("A área do triângulo retângulo é: ",area)