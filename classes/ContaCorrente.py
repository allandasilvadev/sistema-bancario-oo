from classes.Conta import Conta
from classes.Saque import Saque


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        # atributos privados, so serao manipulados pela classe
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\nOperação falhou, O valor do saque excede o limite!\n")
        elif excedeu_saques:
            print("\nOperação falhou, número máximo de saques excedidos!\n")
        else:
            return super().sacar(valor)
        
        return False

    def __str__(self):
        """ Formata a listagem de contas cadastradas. """
        return f"""
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """
