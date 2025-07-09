class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo # variável _saldo é privada,
        #somente poderá ser modificar dentro do escopo da classe
        self.nro_agencia = nro_agencia # variável nro_agencia é pública.

    def depositar(self, valor):
        #...
        self._saldo += valor

    def sacar(self, valor):
        #...
        self._saldo -= valor
    def mostrar_saldo(self):
        #...
        return self._saldo


conta = Conta('0001', 100)
#utilizando método para alterar a variável _saldo que é privada.
#Não podemos alterar a variável PRIVADA diretamente.
conta.depositar(100)

print(conta.nro_agencia)
print(conta.mostrar_saldo())
