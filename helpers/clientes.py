def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf ]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    # se o cliente nao possuir conta cadastrada
    if not cliente.contas:
        print("Cliente não possui contas")
        return
    
    # atualmete nao permite o usuario, escolha a conta
    # usa a primeira conta da lista
    return cliente.contas[0]