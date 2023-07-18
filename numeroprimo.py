
'''
n = int(input('Informe um número:  '))

primos = (2 , 3, 5, 7)

if n < 0 or n == 1:
    print (f"O número {n} não é primo")
elif n in primos:
    print (f"O número {n} é primo")
elif n% 2 == 0 or n%3 == 0 or n%5 == 0  or n%7 == 0:
    print (f"O número {n} não é primo")
else:
    print (f"O número {n} é primo")
'''

n = int(input('Informe um número:  '))

primos = (2 , 3, 5, 7)
div = 0

if n < 0 or n == 1:
    print (f"O número {n} não é primo")
elif n in primos:
    print (f"O número {n} é primo")

for i in range (2, n-1,1):
    div = n%i

if div == 0:
    print (f"O número {n} não é primo")
else:
    print (f"O número {n} é primo")


