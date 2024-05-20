from helpers.clientes import filtrar_cliente
from classes.ContaCorrente import ContaCorrente


def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o cpf do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    # se o cliente nao existir interrompe o processo de criacao de conta
    if not cliente:
        print("Cliente não encontrado, fluxo de criação de conta encerrado!")
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)

    # adiciona  a conta criada a lista de contas
    contas.append(conta)

    # um cliente podera ter mais de uma conta
    cliente.contas.append(conta)

    print("\nConta criada com sucesso!\n")