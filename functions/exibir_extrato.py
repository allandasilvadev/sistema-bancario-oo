from helpers.clientes import filtrar_cliente, recuperar_conta_cliente


def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado!\n")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    # exibe o extrato detalhado
    print(" Extrato" .center(60, "="))
    transacoes = conta.historico.transacoes

    extrato = ""

    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}\n"

    print(extrato)
    print(f"\nSaldo: \n\tR$ {conta.saldo:.2f}")

    print("=" * 60)