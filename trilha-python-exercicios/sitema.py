menu_opcoes = """
[1] Depositar
[2] Sacar
[3] Ver Extrato
[4] Sair

Escolha uma opção: """

saldo_atual = 0
limite_diario = 500
registro_extrato = ""
saques_realizados = 0
MAX_SAQUES = 3

while True:
    escolha = input(menu_opcoes)

    if escolha == "1":
        valor_deposito = float(input("Digite o valor para depósito: "))

        if valor_deposito > 0:
            saldo_atual += valor_deposito
            registro_extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        else:
            print("Erro! Valor de depósito inválido.")

    elif escolha == "2":
        valor_saque = float(input("Digite o valor para saque: "))

        saldo_insuficiente = valor_saque > saldo_atual
        limite_excedido = valor_saque > limite_diario
        saques_excedidos = saques_realizados >= MAX_SAQUES

        if saldo_insuficiente:
            print("Erro! Saldo insuficiente.")

        elif limite_excedido:
            print("Erro! Saque acima do limite diário.")

        elif saques_excedidos:
            print("Erro! Número máximo de saques atingido.")

        elif valor_saque > 0:
            saldo_atual -= valor_saque
            registro_extrato += f"Saque: R$ {valor_saque:.2f}\n"
            saques_realizados += 1

        else:
            print("Erro! Valor de saque inválido.")

    elif escolha == "3":
        print("\n=========== EXTRATO ===========")
        print("Nenhuma movimentação realizada." if not registro_extrato else registro_extrato)
        print(f"\nSaldo atual: R$ {saldo_atual:.2f}")
        print("===============================")

    elif escolha == "4":
        break

    else:
        print("Opção inválida, tente novamente.")






        
                