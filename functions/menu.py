import textwrap


def menu():
    """ Cria o menu inicial """
    dados = """\n
    ==================== MENU ====================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nu]\tNovo usuário
    [nc]\tNova conta
    [lc]\tListar contas
    [q]\tSair
    ==============================================
    """
    return input(textwrap.dedent(dados))
