
salario = float(input("Informe o salário: ").replace(",","."))

if salario < 1903.98:
    print ("Salário bruto: R$ {} \nIsento de IRPF".format(salario))
elif salario >= 1903.98 and salario <= 2826.65:
    deducao = (salario*0.075)-142.80
    liquido = salario - deducao
    print ("Salário bruto: R$ {} \nDedução: R$ {} \nSalário líquido: R$ {} ".format(salario,deducao,liquido))
elif salario >= 2826.66 and salario <= 3751.05:
    deducao = (salario*0.15)-354.80
    liquido = salario - deducao
    print ("Salário bruto: R$ {} \nDedução: R$ {} \nSalário líquido: R$ {} ".format(salario,deducao,liquido))
elif salario >= 3751.06 and salario <= 4664.68:
    deducao = (salario*0.225)-636.13
    liquido = salario - deducao
    print ("Salário bruto: R$ {} \nDedução: R$ {} \nSalário líquido: R$ {} ".format(salario,deducao,liquido))
else:
    deducao = (salario*0.275)-869.36
    liquido = salario - deducao
    print ("Salário bruto: R$ {} \nDedução: R$ {} \nSalário líquido: R$ {} ".format(salario,deducao,liquido))
