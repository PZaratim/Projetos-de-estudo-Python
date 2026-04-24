ultimo_resultado = None

while True:
    try:
        if ultimo_resultado is not None:
            while True:
                usar = input("Usar último resultado? (s/n): ").lower()
                if usar in ["s", "sim"]:
                    valor1 = ultimo_resultado
                    break
                elif usar in ["n", "não", "nao"]:
                    valor1 = float(input("Digite o primeiro valor: "))
                    break
                else:
                    print("Digite apenas 's' ou 'n'")
        else:
            valor1 = float(input("Digite o primeiro valor: "))

        valor2 = float(input("Digite o segundo valor: "))

        # MENU
        print("\n=== CALCULADORA ===")
        print("[+] Soma")
        print("[-] Subtração")
        print("[*] Multiplicação")
        print("[/] Divisão")
        print("[%] Resto")
        print("[**] Potência")
        print("[sqrt] Raiz quadrada")
        print("[sair] Encerrar")

        operacao = input("Escolha a operação: ").lower()

        # OPERAÇÕES
        if operacao == "+":
            resultado = valor1 + valor2

        elif operacao == "-":
            resultado = valor1 - valor2

        elif operacao == "*":
            resultado = valor1 * valor2

        elif operacao == "/":
            if valor2 == 0:
                print("Erro: divisão por zero!")
                print("--------------------------------")
                continue
            resultado = valor1 / valor2

        elif operacao == "%":
            if valor2 == 0:
                print("Erro: divisão por zero!")
                print("--------------------------------")
                continue
            resultado = valor1 % valor2

        elif operacao == "**":
            resultado = valor1 ** valor2

        elif operacao == "sqrt":
            if valor1 < 0:
                print("Erro: raiz de número negativo!")
                print("--------------------------------")
                continue
            resultado = valor1 ** 0.5

        elif operacao == "sair":
            print("Encerrando a calculadora...")
            break

        else:
            print("Operação inválida!")
            print("--------------------------------")
            continue

        # RESULTADO
        print(f"Resultado: {resultado:.2f}")
        print("--------------------------------")

        ultimo_resultado = resultado

    except ValueError:
        print("Erro: digite apenas números!")
        print("--------------------------------")