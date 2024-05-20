from helpers.clientes import filtrar_cliente, recuperar_conta_cliente
from classes.Deposito import Deposito


def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    # se o cliente nao foi encontrado, finaliza o processo de saque.
    if not cliente:
        print("\nCliente não encontrado\n")
        return
    
    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)
