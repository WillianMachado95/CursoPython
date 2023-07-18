print ("\nPENSE EM UM NÚMERO DE 0 A 10\n*****************************")

p1 = input('O número que você pensou é par? ')
if p1 == "sim":
    p2 = input('O número que você pensou é menor que 5?: ')
    if p2 == "sim":
        p3 = input('O número que você pensou é um número primo: ')
        if p3 == "sim":
             print("O NÚMERO QUE VOCÊ PENSOU É 2 (＾∇＾)")
        else:
              print("O NÚMERO QUE VOCÊ PENSOU É 4 (＾∇＾)")
    else:
         p3 = input('O número que você pensou é menor que 7?: ')
         if p3 == "sim":
            print("O NÚMERO QUE VOCÊ PENSOU É 6 (＾∇＾)")
         elif p3 == "não":
            p4 = input('O número que você pensou é o dobro de 4?: ')
            if p4 == "sim":
                print("O NÚMERO QUE VOCÊ PENSOU É 8 (＾∇＾)")
            else:
                print("O NÚMERO QUE VOCÊ PENSOU É 10 (＾∇＾)")
else: 
    p2 = input('O número que você pensou é menor que 4?  ')
    if p2 == "sim":
       p3 = input(' O número que você pensou seria 3?   ')
       if p3 == "sim":
           print ("FÁCIL, NÚMERO QUE VOCÊ PENSOU É 3 (ᴗ˳ᴗ)")
       else:
           print ("ENTÃO NÚMERO QUE VOCÊ PENSOU É 1 (＾∇＾)")
    else:
        p3 = input(' O número que você pensou é maior que 6? ')
        if p3 == "sim":
            p4 = input ("O número que você pensou seria 7? ")
            if p4 == "sim":
                print ("FÁCIL, NÚMERO QUE VOCÊ PENSOU É 7  (ᴗ˳ᴗ)")
            else:
                print ("FÁCIL, ENTÃO O NÚMERO QUE VOCÊ PENSOU É 9  (ᴗ˳ᴗ)")
        else:
            print ("FÁCIL, NÚMERO QUE VOCÊ PENSOU É 5 (-_-) zzz")
