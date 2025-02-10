def main():
    saldo = 0
    limite_por_saque = 500
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        print("\n--- Sistema Bancário ---")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor a ser depositado: R$ "))
            if valor > 0:
                saldo += valor
                extrato.append(f"Depósito: R$ {valor:.2f}")
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Valor inválido! O valor do depósito deve ser positivo.")

        elif opcao == "2":
            if numero_saques >= LIMITE_SAQUES:
                print("Limite diário de saques atingido.")
            else:
                valor = float(input("Digite o valor a ser sacado: R$ "))
                if valor > 0:
                    if valor > limite_por_saque:
                        print(f"Limite máximo por saque é de R$ {limite_por_saque:.2f}.")
                    elif valor > saldo:
                        print("Saldo insuficiente para realizar o saque.")
                    else:
                        saldo -= valor
                        extrato.append(f"Saque: R$ {valor:.2f}")
                        numero_saques += 1
                        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
                else:
                    print("Valor inválido! O valor do saque deve ser positivo.")

        elif opcao == "3":
            print("\n--- Extrato ---")
            if not extrato:
                print("Não foram realizadas movimentações.")
            else:
                for movimentacao in extrato:
                    print(movimentacao)
            print(f"Saldo atual: R$ {saldo:.2f}")

        elif opcao == "4":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()