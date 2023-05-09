# define uma função para exibir o menu
def exibir_menu():
    print("Escolha uma opção: ")
    print("\n1 - Registrar venda de vendedor 1")
    print("\n2 - Registrar venda de vendedor 2")
    print("\n3 - Registrar venda de vendedor 3")
    print("\n4 - Exibir total de vendas de todos os vendedores")
    print("\n5 - Sair do programa")

# inicializa as variáveis de venda de cada vendedor como zero
vendas_vendedor1 = 0
vendas_vendedor2 = 0
vendas_vendedor3 = 0

# loop principal do programa
while True:
    exibir_menu()
    opcao = input("\nDigite o número da opção desejada: ")

    # registra a venda do vendedor 1
    if opcao == "1":
        valor_venda = float(input("Digite o valor da venda: "))
        vendas_vendedor1 += valor_venda
        print("Venda registrada com sucesso.")

    # registra a venda do vendedor 2
    elif opcao == "2":
        valor_venda = float(input("Digite o valor da venda: "))
        vendas_vendedor2 += valor_venda
        print("Venda registrada com sucesso.")

    # registra a venda do vendedor 3
    elif opcao == "3":
        valor_venda = float(input("Digite o valor da venda: "))
        vendas_vendedor3 += valor_venda
        print("Venda registrada com sucesso.")

    # exibe o total de vendas de todos os vendedores
    elif opcao == "4":
        total_vendas = vendas_vendedor1 + vendas_vendedor2 + vendas_vendedor3
        print(f"\nTotal de vendas:\nVendedor 1: R${vendas_vendedor1:.2f}\nVendedor 2: R${vendas_vendedor2:.2f}\nVendedor 3: R${vendas_vendedor3:.2f}\nTotal: R${total_vendas:.2f}")
        if total_vendas>=500000:
            print('\nMeta nv 1 atingida, todos ganharam 1 dia de folga')
        elif total_vendas >= 750000:
            print('\nMeta nv 2 atingida, todos ganham um final de semana em hotel com tudo pago nas férias')
        elif total_vendas > 1000000:
            print('\nMeta nv máximo, todos ganham a direito 1 por cento da PL final do ano') 

    # sai do programa
    elif opcao == "5":
        print("Programa encerrado.")
        break

    # opção inválida
    else:
        print("Opção inválida. Tente novamente.")
