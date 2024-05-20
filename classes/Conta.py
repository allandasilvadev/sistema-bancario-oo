from classes.Historico import Historico


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\nOperação falhou, você não tem saldo suficiente.\n")
        elif valor > 0:
            self._saldo -= valor
            print("\nSaque realizado com sucesso!\n")
            return True
        else:
            print("\nOperação falhou, o valor informado é inválido!\n")
        
        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\nDepósito realizado com sucesso.\n")
        else:
            print("\nNão foi possível realizar o depósito, o valor informado é inválido.\n")
            return False
        
        return True
    