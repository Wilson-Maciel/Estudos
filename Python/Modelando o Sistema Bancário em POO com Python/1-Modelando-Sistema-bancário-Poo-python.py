from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime
import textwrap

#Criando a classe cliente
class Cliente:
    #inicializando a classe
    def __init__(self, endereço):
        self.endereço = endereço
        self.contas = []
        self.indice_conta = 0

    #Criando os métodos
    #Método realizando transação
    def realizar_transacao(self, conta, transacao):
        if len(conta.historico.transacoes_do_dia()) >= 10:
            print("\n@@@ Você excedeu o número de transações permitidas para hoje! @@@")
            return
        transacao.registrar(conta)

    #Criando método adicionar_conta
    def adicionar_conta(self, conta):
        self.contas.append(conta)

#Agora vamos criar a classe PessoaFisica que herda da classe Cliente
class PessoaFisica(Cliente):
    #inicializar a classe
    def __init__(self, cpf, nome, data_nascimento, endereco):
        #atribuir ao atributo endereço o endereço da classe pai
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


class Conta:
    #inicialisamos a conta
    def __init__(self, numero, cliente):
        #criar o atributo saldo como PRIVADO _saldo
        self._saldo = 0
        #criar o atributo numero como PRIVADO _numero
        self._numero = numero
        #criar o atributo agencia como PRIVADO _agencia
        self._agencia = "0001"
        #criar o atributo cliente como PRIVADO _cliente
        self._cliente = cliente
        #Criar o atributo hostórico como PRIVADO e chamar o método histórico
        self._historico = Historico

    #Criando um método somente para a classe
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    #Criando propriedades para acessar os atributos privados com segurança

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

    #Criando o método sacar
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print(f"\n@@@ Operação falhou! O valor informado é inválido. @@@")


        elif valor > 0:
            self._saldo -= valor
            print(f"\n--- Saque realizado com sucesso! ---  ")
            return True

        else:
            print(f"\n@@@ Operação falhou! O valor informado é inválido. @@@")
        #esse retorno falso serve para o if e para o else, ou seja, uma lógica de exclusão,
        # caso não caixa no elif com o retorno True, o retorno será False.
        return False

    def depositar(self, valor):
        if valor > 0:
           self._saldo += valor
           print(f"\n--- Deposito realizado com sucesso! ---")
           return True
        else:
           print(f"\n@@@ Operação falhou! O valor informado é inválido.")
           return False


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
    def sacar(self, valor):
        #pegar q quantidade de saque no método hitórico
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes
            if transacao["tipo"]== Saque.__name__]
        )
    #sitaxe equivalente
    #saques_filtrados = []
    #for transacao in self.historico.transacoes:
    #if transacao["tipo"] == Saque.__name__:
    #saques_filtrados.append(transacao)
    #numero_saques = len(saques_filtrados)
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self
        limite_saques

        if excedeu_limite:
            print(f"\n@@@ Operação falhou! O valor do saque excedido. @@@")

        elif excedeu_saques:
            print(f'\n @@@ Operação falhou! Número máximo de saques excedido. @@@')

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C: \t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._trasacoes = [] # armazena todas transações

    @property
    def trasacoes(self):
        return self._trasacoes

    def adicionar_transacao(self, transacao):
        self._transacao.append(
            {
                "tipo": transacao.__class__.__nome__,
                "valor": transacao.valor,
                "data": datetime.utcnow().strftime
                ("%d-%m-%Y %H:%M:%s"),
            }
        )

        def gerar_relatorio(self. tipo_transacao=None):
            for transacao in self._transacoes:
                if tipo_transacao is None or trasacao["tipo"].lower() == tipo_transacao.lower():
                    yield transacao

        def transacoes_do_dia(self):
            data_atual = datetime.utcnow().date # retornar a data atual
            transacoes = []                     #guardar as transações do mesmo dia.
            for transacao in self._transacoes:  #percorrer todas as transações armazenadas no atributo privado.
                data_transacao = datetime.strptime(transacao["data"], "%d-%m-%Y %H:%M:%S").date() # converter a data e hora da transação para datetime, somente a data
                if data_atual == data_transacao:
                    transacoes.append(transacao)

            return transacoes







#definindo classe abstrata
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self,valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def regstrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self,valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print(f"\n@@@ Cliente não possui conta! @@@")
        return
    #FIXME: não permite cliente escolher a conta
    return cliente.contas[0]

def sacar(clientes):
    cpf = input("Informe o cpf do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print(f"\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o cpf do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print(f"\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print(f"\n==========================EXTRATO==========================")
    extrato = " "

    tem_transacao = False
    for transacao in conta.historico.gerar_relatorio():
        tem_transacao = Trueextrato += f"\n{transacao["data"]}\n{transacao["tipo"]}:\n\tR$ {transacao["valor"]:.2f} "
    if not tem_transacao:
        extrato = "Não foram realizadas movimentações."
    

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("===================================================")

def criar_cliente(clientes):
    cpf = input("Informe o cpf do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print(f"\n@@@ Já existe cliente com essse CPF! @@@")
        return

    nome = input(" Informe o nome completo: ")
    data_nascimento = input(f"Informe a data de nascimento (dd-mm-aaa): ")
    endereco = input(f" Informe o endereço ( logradouro, nro - bairro - cidade/sigla do estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! === ")

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o cpf do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print(f"\n@@@ Cliente não encontrado, fluxo de ciação de conta encerrado! @@@")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente,numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print(f"\n === Conta criada com sucesso! === ")

def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))

def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print(f"\n@@@ Cliente não encontrado! @@@")
        return
    valor = float(input(f"Informe o valor do depósito:"))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    cliente.realizar_transacao(conta, transacao)


def menu():
    menu = """\n
    ================MENU================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair
    =>"""
    return input(textwrap.dedent(menu))


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nu":
            criar_cliente(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada.@@@ ")

main()
