a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))



delta = (b ** 2) - 4 * a * c

if delta < 0:
    print ("Equação sem raízes reais")
elif delta == 0:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    print(" X1: ",x1)
else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

    print("raízes = x1: {}, x2: {}".format(x1, x2))