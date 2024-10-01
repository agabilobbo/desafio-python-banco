#Este código implementa uma aplicação básica de banco que permite aos usuários realizar operações típicas
#como depósitos, saques, e consulta de extratos, bem como gerenciar usuários e contas.
import textwrap

#Exibe o menu principal e retorna a opção selecionada pelo usuário.
#textwrap.dedent(menu): Remove a indentação do texto, mantendo a formatação.
def menu():
    menu = """\n
    ================ MENU ================
    [1]\tNovo usuário
    [2]\tNova conta
    [3]\tDepositar
    [4]\tSacar
    [5]\tExtrato
    [6]\tListar Contas
    [7]\tSair
    => """
    return input(textwrap.dedent(menu))

#Adiciona um valor ao saldo e registra a operação no extrato se o valor for positivo.
#/: Indica que todos os parâmetros a seguir são posicionais, não podem ser usados como argumentos nomeados.
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        print("\n==== Depósito realizado com sucesso! ====")
    else:
        print("\n@@@ O valor informado é inválido! @@@")
    return saldo, extrato

#Realiza um saque se as condições são atendidas (saldo suficiente, limite não excedido, e número de saques dentro do limite).
#*: Indica que todos os parâmetros a seguir são nomeados, não podem ser usados como argumentos posicionais.

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Saldo insuficiente! @@@")

    elif excedeu_limite:
        print("\n@@@ Limite excedido! @@@")

    elif excedeu_saques:
        print("\n@@@ Número de saques excedido! @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n==== Saque realizado com sucesso! ====")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido! @@@")

    return saldo, extrato

#xibe o extrato das transações e o saldo atual.
#/ e *: Controlam como os argumentos podem ser passados (por posição ou por nome).
def exibir_extrato (saldo, /, *, extrato):
    print("\n========== EXTRATO ==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("========== FINALIZADO ==========")

#Cria um novo usuário, adicionando-o à lista usuarios se o CPF não existir.
def criar_usuário(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Usuário ja existe! @@@")
        return

    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n==== Usuário criado com sucesso! ====")

#Filtra e retorna o usuário com o CPF fornecido, se existir.
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

#Cria uma nova conta se o usuário existir, associando a conta ao usuário filtrado.
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("informe o CPF do usuário:")  
    usuario = filtrar_usuario(cpf,usuarios) 

    if usuario:
        print("\n=== Conta criada com sucesso ===")
        return { "agencia": agencia, "numero_conta": numero_conta, "usuario": usuario }	
        
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado @@@")

  #Lista todas as contas existentes, formatando a exibição com textwrap.dedent para remover a indentação.             
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência:\t{conta["agencia"]}
        C/C:\t\t{conta["numero_conta"]}
        Titular:\t{conta["usuario"]["nome"]}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


#main(): Função principal que inicializa variáveis e executa um loop de interação com o usuário.
#LIMITE_SAQUES e AGENCIA: Definem o limite de saques e o código da agência.
#saldo, limite, extrato, numero_saques, usuarios, contas: Variáveis que armazenam o estado atual do sistema.
#while True: Loop que exibe o menu e executa ações baseadas na opção escolhida pelo usuário.

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            criar_usuário(usuarios)

        elif opcao == "2":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "3":    
            valor = float(input("Qual valor deseja depositar? "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "4":
            valor = float(input("Qual valor deseja sacar? "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato, 
                limite=limite, 
                numero_saques=numero_saques, 
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "5":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "7":
            break
main()

        