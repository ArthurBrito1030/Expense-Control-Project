print("CONTROLE DE DESPESAS")

despesas = []

opcao = ""

def registrar_despesa(despesas):
    while True:
        descricao = input("Digite a descrição da despesa: ").strip()
        if descricao == "":
            print("A descrição não pode ser vazia.")
            continue
        break

    while True:
        try:
            valor = float(input("Digite o valor da despesa: "))
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")
            continue
        if valor <= 0:
            print("O valor deve ser maior que zero.")
            continue
        despesas.append([descricao, valor])
        print("Despesa registrada com sucesso!")
        

def listar_despesas(despesas):
    if not despesas:
        print("Nenhuma despesa registrada.")
    else:
        print("Despesas registradas:")
        for despesa in despesas:
            print(f"{despesa[0]}: R${despesa[1]:.2f}")

def consultar_total_gasto(despesas):
    total = sum(despesa[1] for despesa in despesas)
    return total

while opcao != "4":
    print("1 - Registrar despesa")
    print("2 - Listar despesas")
    print("3 - Consultar total gasto")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        registrar_despesa(despesas)

    elif opcao == "2":
        listar_despesas(despesas)

    elif opcao == "3":
        total_gasto = consultar_total_gasto(despesas)
        print(f"Total gasto: R${total_gasto:.2f}")

    elif opcao == "4":
        print("Saindo do programa...")

    else:
        print("Opção inválida")



