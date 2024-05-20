from functions.menu import menu
from functions.criar_cliente import criar_cliente


def main():
    clientes = []

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
            pass

        elif opcao == "lc":
            pass

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor, selecione novamente a operação desejada!")


main()