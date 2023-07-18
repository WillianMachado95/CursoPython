
m = int(input("Digite o valor da massa: "))
c = 300000000
e = m*(c*c)

resultado = '{0:,}'.format(e).replace(',','.')

print(resultado) 