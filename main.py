from functions.menu import menu
from functions.criar_cliente import criar_cliente
from functions.criar_conta import criar_conta
from functions.listar_contas import listar_contas
from functions.depositar import depositar
from functions.sacar import sacar
from functions.exibir_extrato import exibir_extrato


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

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