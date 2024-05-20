from functions.menu import menu
from functions.criar_cliente import criar_cliente
from functions.criar_conta import criar_conta
from functions.listar_contas import listar_contas


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            pass

        elif opcao == "s":
            pass

        elif opcao == "e":
            pass

        elif opcao == "nu":
            criar_cliente(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor, selecione novamente a operação desejada!")


main()