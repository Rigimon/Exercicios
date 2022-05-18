#loop
#Exercicio 1
for i in range (1,41):
    name = str(input("Nome do Aluno:"))
    n1 = float(input("Nota 1:"))
    n2 = float(input("Nota 2:"))
    print ("Média:",(n1+n2)/2)
    print()

#exercicio 2
cont = 100
while (cont > -1):
    print (cont)
    cont = cont - 1

#Exercicio 3
cont = 0
while (cont < 101):
    if (cont % 2 == 0):
        print (cont)
    cont = cont + 1

#Exercicio 4
cont = 0
neg = 0
pos = 0
while (cont < 10):
    num = int(input("Digite um número:"))
    if (num < 0):
        neg = neg + 1
    else:
        pos = pos + 1
    cont = cont + 1
print ("Negativos:",neg)
print ("Positivos:",pos)
    
#Exercicio 5
print ("Quantos alunos tem nessa classe")
q = int(input())
for i in range (1,q+1):
    n1 = float(input("Nota 1:"))
    n2 = float(input("Nota 2:"))
    print ("Média:",(n1+n2)/2)

#Exercicio 7
print ()
n1 = int(input("Digite um número:"))
while True:
    n2 = int(input("Digite um número:"))
    if (n2 != 0):
        break
print ("Valor da Divisão",n1/n2)

#Exercicio 8
while True:
    n1 = float(input("Digite a 1°Nota:"))
    if (n1 < 10) and (n1 > 0):
        break
    else:
        print ("Nota Invalida")
while True:
    n2 = float(input("Digite a 2°Nota:"))
    if (n2 > 0) and (n2 < 10):
        break
    else:
        print ("Nota Invalida")
print ("Média:",(n1+n2)/2)
