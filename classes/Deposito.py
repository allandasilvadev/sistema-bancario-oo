from classes.Transacao import Transacao


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        successo_transacao = conta.depositar(self.valor)

        if successo_transacao:
            conta.historico.adicionar_transacao(self)