from classes.Conta import Conta


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        # atributos privados, so serao manipulados pela classe
        self._limite = limite
        self._limite_saques = limite_saques

    def __str__(self):
        """ Formata a listagem de contas cadastradas. """
        return f"""
            Agência:\t{self.agencia}
            C/C:\t\t{self._numero}
            Titular:\t{self.cliente.nome}
        """
