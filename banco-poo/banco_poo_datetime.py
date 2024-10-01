import textwrap 
from abc import ABC, abstractmethod
from datetime import datetime

class ContasIterador:
    """
    Iterador para percorrer as contas bancárias.
    Permite a iteração sobre as contas de forma personalizada.
    """
    def __init__(self, contas):
        """
        Inicializa o iterador de contas.

        :param contas: Lista de contas a serem iteradas.
        """
        self.contas = contas
        self._index = 0  # Índice inicial do iterador

    def __iter__(self):
        """
        Retorna o iterador em si, permitindo a iteração.
        
        :return: O próprio iterador.
        """
        return self

    def __next__(self):
        """
        Retorna a próxima conta no iterador, formatada.
        
        :return: String formatada da conta.
        :raises StopIteration: Quando não há mais contas a serem iteradas.
        """
        try:
            conta = self.contas[self._index]  # Obtém a conta atual
            return f"""\nAgência:\t{conta.agencia}\nNúmero:\t\t{conta.numero}\nTitular:\t{conta.cliente.nome}\nSaldo:\t\tR${conta.saldo:.2f}"""
        except IndexError:
            raise StopIteration  # Indica que não há mais contas
        finally:
            self._index += 1  # Move para a próxima conta

class Cliente:
    """
    Classe que representa um cliente do banco.
    Um cliente pode ter várias contas e realizar transações.
    """
    def __init__(self, endereco):
        """
        Inicializa o cliente com um endereço e uma lista de contas.

        :param endereco: Endereço do cliente.
        """
        self.endereco = endereco
        self.contas = []  # Lista de contas do cliente

    def realizar_transacao(self, conta, transacao):
        """
        Realiza uma transação (saque ou depósito) na conta do cliente.
        Limita o número de transações por dia.

        :param conta: A conta em que a transação será realizada.
        :param transacao: A transação a ser registrada (saque ou depósito).
        """
        if len(conta.historico.transacoes_do_dia()) >= 2:
            print("\n@@@ Você excedeu o número de transações permitidas para hoje! @@@")
            return
        transacao.registrar(conta)  # Registra a transação na conta

    def adicionar_conta(self, conta):
        """
        Adiciona uma conta à lista de contas do cliente.

        :param conta: A conta a ser adicionada.
        """
        self.contas.append(conta)  # Adiciona a conta à lista

class PessoaFisica(Cliente):
    """
    Representa um cliente pessoa física.
    Herda da classe Cliente e adiciona informações específicas.
    """
    def __init__(self, nome, data_nascimento, cpf, endereco):
        """
        Inicializa o cliente pessoa física com nome, data de nascimento, CPF e endereço.

        :param nome: Nome do cliente.
        :param data_nascimento: Data de nascimento do cliente.
        :param cpf: CPF do cliente.
        :param endereco: Endereço do cliente.
        """
        super().__init__(endereco)  # Chama o construtor da classe pai
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    """
    Classe que representa uma conta bancária.
    Possui saldo, número, agência e histórico de transações.
    """
    def __init__(self, numero, cliente):
        """
        Inicializa uma conta com número, cliente, agência fixa e histórico.

        :param numero: Número da conta.
        :param cliente: Cliente associado à conta.
        """
        self._saldo = 0  # Inicializa o saldo como 0
        self._numero = numero
        self._agencia = "0001"  # Agência fixa
        self.cliente = cliente
        self._historico = Historico()  # Inicializa o histórico de transações

    @property
    def saldo(self):
        """
        Retorna o saldo da conta.

        :return: Saldo atual da conta.
        """
        return self._saldo

    @property
    def agencia(self):
        """
        Retorna a agência da conta.

        :return: Agência da conta.
        """
        return self._agencia

    @property
    def numero(self):
        """
        Retorna o número da conta.

        :return: Número da conta.
        """
        return self._numero

    @property
    def historico(self):
        """
        Retorna o histórico da conta.

        :return: Histórico de transações da conta.
        """
        return self._historico

    def sacar(self, valor):
        """
        Realiza o saque, verificando se o saldo é suficiente.

        :param valor: Valor a ser sacado.
        :return: True se o saque for realizado com sucesso, False caso contrário.
        """
        if valor > self.saldo:
            print("\n@@@ Saldo insuficiente! @@@")
        elif valor > 0:
            self._saldo -= valor  # Deduz o valor do saldo
            print("\n== Saque realizado com sucesso! ===")
            return True
        else:
            print("\n@@@ O valor informado é inválido! @@@")
        return False

    def depositar(self, valor):
        """
        Realiza o depósito na conta.

        :param valor: Valor a ser depositado.
        :return: True se o depósito for realizado com sucesso, False caso contrário.
        """
        if valor > 0:
            self._saldo += valor  # Adiciona o valor ao saldo
            print("\n== Depósito realizado com sucesso! ===")
            return True
        else:
            print("\n@@@ O valor informado é inválido! @@@")
            return False

class ContaCorrente(Conta):
    """
    Classe que representa uma conta corrente.
    Herda da classe Conta e adiciona funcionalidades específicas de conta corrente.
    """
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        """
        Inicializa a conta corrente com um limite de saque e limite de saques diários.

        :param numero: Número da conta.
        :param cliente: Cliente associado à conta.
        :param limite: Limite máximo de saque.
        :param limite_saques: Número máximo de saques permitidos por dia.
        """
        super().__init__(numero, cliente)  # Chama o construtor da classe pai
        self.limite = limite
        self._limite_saques = limite_saques

    @classmethod
    def nova_conta(cls, cliente, numero, limite=500, limite_saques=3):
        """
        Cria uma nova conta corrente.

        :param cliente: Cliente associado à nova conta.
        :param numero: Número da nova conta.
        :param limite: Limite máximo de saque.
        :param limite_saques: Número máximo de saques permitidos por dia.
        :return: Instância da nova ContaCorrente.
        """
        return cls(numero, cliente, limite, limite_saques)

    def sacar(self, valor):
        """
        Realiza o saque, respeitando o limite e número de saques diários.

        :param valor: Valor a ser sacado.
        :return: True se o saque for realizado com sucesso, False caso contrário.
        """
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        if valor > self.limite:
            print("\n@@@ O valor do saque excede o limite! @@@")
        elif numero_saques >= self._limite_saques:
            print("\n@@@ Número de saques excedido! @@@")
        elif valor > 0:
            self._saldo -= valor  # Deduz o valor do saldo
            print("\n== Saque realizado com sucesso! ===")
            return True
        else:
            return super().sacar(valor)  # Chama o método da classe pai para saques válidos
        return False

    def __str__(self):
        """
        Retorna uma string formatada com os dados da conta corrente.

        :return: String com informações da conta corrente.
        """
        return f"\nAgência:\t{self.agencia}\nC/C:\t\t{self.numero}\nTitular:\t{self.cliente.nome}\nSaldo:\t\tR${self.saldo:.2f}"

class Historico:
    """
    Classe que armazena o histórico de transações da conta.
    Permite registrar e consultar transações realizadas.
    """
    def __init__(self):
        """
        Inicializa a lista de transações.
        """
        self._transacoes = []  # Lista para armazenar transações

    @property
    def transacoes(self):
        """
        Retorna as transações registradas.

        :return: Lista de transações.
        """
        return self._transacoes

    def adicionar_transacao(self, transacao):
        """
        Adiciona uma transação ao histórico.

        :param transacao: Transação a ser adicionada.
        """
        self._transacoes.append(
            {"tipo": transacao.__class__.__name__, "valor": transacao.valor, "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")}
        )  # Adiciona transação com tipo, valor e data

    def gerar_relatorio(self):
        """
        Gera o relatório de todas as transações.

        :yield: Cada transação registrada.
        """
        for transacao in self.transacoes:
            yield transacao

    def transacoes_do_dia(self):
        """
        Retorna as transações realizadas no dia atual.

        :return: Lista de transações do dia.
        """
        data_atual = datetime.now().strftime("%d-%m-%Y")
        return [transacao for transacao in self.transacoes if transacao["data"].startswith(data_atual)]

class Transacao(ABC):
    """
    Classe abstrata para representar transações financeiras.
    Define a interface para saques e depósitos.
    """
    @property
    @abstractmethod
    def valor(self):
        """
        Retorna o valor da transação.

        :return: Valor da transação.
        """
        pass

    @abstractmethod
    def registrar(self, conta):
        """
        Registra a transação na conta.

        :param conta: Conta na qual a transação será registrada.
        """
        pass

class Saque(Transacao):
    """
    Classe para representar a operação de saque.
    Implementa a lógica de registro de um saque.
    """
    def __init__(self, valor):
        """
        Inicializa o saque com um valor.

        :param valor: Valor a ser sacado.
        """
        self._valor = valor

    @property
    def valor(self):
        """
        Retorna o valor do saque.

        :return: Valor do saque.
        """
        return self._valor

    def registrar(self, conta):
        """
        Registra o saque na conta se for bem-sucedido.

        :param conta: Conta na qual o saque será registrado.
        """
        if conta.sacar(self.valor):  # Tenta realizar o saque
            conta.historico.adicionar_transacao(self)  # Adiciona ao histórico

class Deposito(Transacao):
    """
    Classe para representar a operação de depósito.
    Implementa a lógica de registro de um depósito.
    """
    def __init__(self, valor):
        """
        Inicializa o depósito com um valor.

        :param valor: Valor a ser depositado.
        """
        self._valor = valor

    @property
    def valor(self):
        """
        Retorna o valor do depósito.

        :return: Valor do depósito.
        """
        return self._valor

    def registrar(self, conta):
        """
        Registra o depósito na conta se for bem-sucedido.

        :param conta: Conta na qual o depósito será registrado.
        """
        if conta.depositar(self.valor):  # Tenta realizar o depósito
            conta.historico.adicionar_transacao(self)  # Adiciona ao histórico

def log_transacao(func):
    """
    Decorador para logar as transações realizadas.
    Captura a hora da transação e exibe no console.

    :param func: Função a ser decorada.
    :return: Função decorada.
    """
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)  # Chama a função original
        print(f"{datetime.now()}: {func.__name__.upper()}")  # Loga a transação
        return resultado
    return envelope

def menu():
    """
    Exibe o menu e captura a opção selecionada pelo usuário.
    
    :return: Opção selecionada pelo usuário.
    """
    menu = """\n
    ========= MENU =========
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tCriar cliente
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))  # Exibe o menu e captura a entrada

def filtrar_cliente(cpf, clientes):
    """
    Filtra um cliente pelo CPF.

    :param cpf: CPF do cliente a ser filtrado.
    :param clientes: Lista de clientes a ser filtrada.
    :return: Cliente correspondente ao CPF ou None se não encontrado.
    """
    return next((cliente for cliente in clientes if cliente.cpf == cpf), None)  # Retorna o cliente ou None

def recuperar_conta_cliente(cliente):
    """
    Retorna a primeira conta do cliente.

    :param cliente: Cliente do qual recuperar a conta.
    :return: Primeira conta do cliente ou None se não houver.
    """
    return cliente.contas[0] if cliente.contas else None  # Retorna a primeira conta ou None se não houver

@log_transacao
def depositar(clientes):
    """
    Realiza um depósito na conta de um cliente.

    :param clientes: Lista de clientes do sistema.
    """
    cpf = input("CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Esse cliente não existe! @@@")
        return

    valor = float(input("Valor a ser depositado: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)  # Realiza a transação de depósito

@log_transacao
def sacar(clientes):
    """
    Realiza um saque na conta de um cliente.

    :param clientes: Lista de clientes do sistema.
    """
    cpf = input("CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Esse cliente não existe! @@@")
        return

    valor = float(input("Valor a ser sacado: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)  # Realiza a transação de saque

@log_transacao
def exibir_extrato(clientes):
    """
    Exibe o extrato da conta de um cliente.

    :param clientes: Lista de clientes do sistema.
    """
    cpf = input("CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Esse cliente não existe! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("\n========== EXTRATO ==========")
    extrato = ""
    transacoes = conta.historico.gerar_relatorio()  # Gera o relatório de transações

    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\tR${transacao['valor']:.2f}\t Data: {transacao['data']}"
    
    print(extrato)
    print(f"\nSaldo:\t\tR${conta.saldo:.2f}")
    print("==============================")

@log_transacao
def criar_cliente(clientes):
    """
    Cria um novo cliente e o adiciona à lista de clientes.

    :param clientes: Lista de clientes do sistema.
    """
    cpf = input("Informe o CPF (somente números): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n@@@ Já existe um cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço: ")

    cliente = PessoaFisica(nome, data_nascimento, cpf, endereco)  # Cria um novo cliente
    clientes.append(cliente)  # Adiciona o cliente à lista

    print("\n=== Cliente criado com sucesso! ===")

@log_transacao
def criar_conta(numero_conta, clientes, contas):
    """
    Cria uma nova conta para um cliente.

    :param numero_conta: Número da nova conta.
    :param clientes: Lista de clientes do sistema.
    :param contas: Lista de contas do sistema.
    """
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)  # Cria nova conta
    cliente.adicionar_conta(conta)  # Adiciona a conta ao cliente
    contas.append(conta)  # Adiciona a conta à lista de contas

    print("\n=== Conta criada com sucesso! ===")

@log_transacao
def listar_contas(contas):
    """
    Lista todas as contas cadastradas no sistema.

    :param contas: Lista de contas do sistema.
    """
    if not contas:
        print("\n@@@ Não existem contas cadastradas! @@@")
    else:
        print("\n=== Listagem de Contas ===")
        iterador = ContasIterador(contas)
        for conta in iterador:
            print(conta)  # Mostra as informações da conta
        print("===========================")

def main():
    """
    Função principal que executa o sistema bancário interativo.
    Permite ao usuário interagir com o sistema, realizar operações e gerenciar contas e clientes.
    """
    clientes = []  # Lista de clientes cadastrados
    contas = []    # Lista de contas cadastradas
    numero_conta = 1001  # Número inicial da conta
    while True:
        opcao = menu()  # Chama a função menu para obter a opção do usuário

        if opcao == 'd':  # Depositar
            depositar(clientes)  # Chama a função de depósito

        elif opcao == 's':  # Sacar
            sacar(clientes)  # Chama a função de saque

        elif opcao == 'e':  # Extrato
            exibir_extrato(clientes)  # Chama a função de exibição de extrato

        elif opcao == 'nc':  # Nova conta
            criar_conta(numero_conta, clientes, contas)  # Chama a função de criação de conta
            numero_conta += 1  # Incrementa o número da conta

        elif opcao == 'lc':  # Listar contas
            listar_contas(contas)  # Chama a função de listar contas

        elif opcao == 'nu':  # Criar cliente
            criar_cliente(clientes)  # Chama a função de criação de cliente

        elif opcao == 'q':  # Sair
            print("\n=== Saindo do sistema... ===")
            break  # Encerra o loop

        else:
            print("\n@@@ Opção inválida! Tente novamente. @@@")  # Mensagem de erro

if __name__ == "__main__":
    main()  # Executa a função principal ao rodar o script
