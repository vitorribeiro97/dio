conta_normal = False
conta_universitaria = False
cheque_especial = 450
saldo = 2000
saque = 2450


if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com o uso do cheque especial!")
    else:
        print("Não foi possível realizar o saque!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
else:
    print("Sistema não reconheceu seu tipo de conta.")