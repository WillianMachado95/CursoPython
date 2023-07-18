

def main ():
    global ca
    ca = float(input("Digite o valor do cateto A: ").replace(",","."))
    global cb
    cb = float(input("Digite o valor do cateto B: ").replace(",","."))
    perimetro()
    area()


def hipotenusa ():
    ca2 = ca**2
    cb2 = cb**2
    h = (ca2 + cb2)**0.5
    return(h)

def perimetro ():
    h = hipotenusa()
    p = ca+cb+h
    print ("O perímetro do triângulo retângulo é: ",p)

def area ():
    a = (ca*cb)/2
    print ("A área do triângulo retângulo é: ",a)

main()
