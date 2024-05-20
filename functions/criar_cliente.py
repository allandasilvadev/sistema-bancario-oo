from helpers.clientes import filtrar_cliente
from classes.PessoaFisica import PessoaFisica


def criar_cliente(clientes):
    cpf = input("Informe o CPF [somente numeros]: ")
    # verifica se o cpf ja esta cadastrado.
    cliente = filtrar_cliente(cpf, clientes)
    
    # se ja estiver cadastrado, finaliza sem sucesso.
    if cliente:
        print("Já existe um cliente com esse CPF!")
        return
    
    # se nao estiver prossegue com o cadastro.
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento: [dd-mm-aaaa]: ")
    endereco = input("Informe o endereco [logradouro, nro - bairro - cidade - sigla estado]: ")

    # cria o cliente
    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    # adiciona o cliente a lista de clientes
    clientes.append(cliente)

    print("\nCliente cadastrado com sucesso!\n")    
