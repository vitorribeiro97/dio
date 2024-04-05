MAIOR_IDADE = 18
IDADE_ESPECIAL = 16

idade = int(input("Informe sua idade: "))

if idade >= 18:
    print("Maior de idade, pode tirar a CNH.")

if idade < 18:
    print("Menor de idade, não pode tirar a CNH.")



if idade >= 18:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("Menor de idade, não pode tirar a CNH.")



if idade >= 18:
    print("Maior de idade, pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não práticas.")
else:
    print("Não pode tirar a CNH.")

