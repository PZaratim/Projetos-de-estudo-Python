senha_correta = 123
tentativas = 0

while True:
    usuario = int(input("Digite a senha: "))

    if usuario == senha_correta:
        print("Acesso permitido")
        break
    else:
        print("Acesso negado")
        tentativas += 1

    if tentativas >= 3:
        print("Número máximo de tentativas atingido. Acesso bloqueado.")
        break