MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Informe sua idade: "))

#Exemplo1
if idade >= 18:
    print("Maior de idade, pode tirar a CNH")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH")

#Exemplo2
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("Ainda não pode tirar a CNH.")

#Exemplo3
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tira a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aula teórica, mas não pode fazer aula pratica.")
else:
    print("Ainda não poide tirar a CNH")




