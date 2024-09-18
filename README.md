# Sistema de Gerenciamento Bancário em Python
### Este é um sistema básico de gerenciamento bancário desenvolvido em Python. 
O sistema permite criar usuários e contas, realizar depósitos e saques, exibir extratos e listar contas.

### Funcionalidades
Criar Novo Usuário: Adicione um novo usuário ao sistema com informações pessoais.
Criar Nova Conta: Associe uma conta a um usuário existente.
Depositar: Realize depósitos na conta.
Sacar: Realize saques da conta com restrições de saldo e limite de saques.
Exibir Extrato: Visualize o extrato das transações realizadas.
Listar Contas: Liste todas as contas existentes no sistema.

### Estrutura do Código
menu(): Exibe o menu principal e retorna a opção selecionada pelo usuário.
depositar(saldo, valor, extrato): Realiza um depósito, atualizando o saldo e o extrato.
sacar(saldo, valor, extrato, limite, numero_saques, limite_saques): Realiza um saque, verificando saldo, limite e número de saques.
exibir_extrato(saldo, extrato): Exibe o extrato das transações e o saldo atual.
criar_usuário(usuarios): Adiciona um novo usuário à lista de usuários.
filtrar_usuario(cpf, usuarios): Filtra usuários pelo CPF.
criar_conta(agencia, numero_conta, usuarios): Cria uma nova conta para um usuário existente.
listar_contas(contas): Lista todas as contas existentes.

