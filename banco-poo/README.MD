# Sistema Bancário com POO

Este projeto implementa um sistema bancário em Python utilizando conceitos avançados de **Programação Orientada a Objetos (POO)**. O sistema foi desenvolvido com o objetivo de fornecer um gerenciamento eficiente de clientes e contas bancárias, permitindo a execução de operações bancárias comuns como depósito, saque e consulta de extrato, além de oferecer suporte para múltiplas contas associadas a um mesmo cliente.

## Funcionalidades

O sistema oferece uma série de funcionalidades para a administração de contas e transações bancárias:

- **Criação de Usuários**: Usuários podem ser criados no sistema com as seguintes informações:
  - Nome
  - CPF
  - Data de nascimento
  - Endereço (opcional)
  
- **Criação de Contas**: Associada a um usuário, a conta pode ser criada com os seguintes atributos:
  - Agência
  - Número da conta
  - Saldo inicial (opcional)

- **Depósitos**: Permite realizar depósitos em uma conta bancária, aumentando o saldo.

- **Saques**: Saques podem ser realizados desde que o saldo seja suficiente e que não exceda o limite de saques diários.

- **Consulta de Extrato**: Exibe o histórico completo de transações (depósitos e saques) de uma conta específica.

- **Listagem de Contas**: Exibe todas as contas registradas no sistema com seus respectivos detalhes.

## Estrutura do Projeto

O projeto está organizado em módulos e classes para separar responsabilidades e facilitar a manutenção do código.

### Classes Principais

1. **Cliente**
   - Representa um cliente do banco. Cada cliente possui informações pessoais e está associado a uma ou mais contas bancárias.
   - Atributos: `nome`, `cpf`, `data_nascimento`, `endereco`.
   
2. **Conta (classe abstrata)**
   - Representa uma conta bancária. Esta é uma classe abstrata que define os atributos e comportamentos básicos de uma conta.
   - Atributos: `agencia`, `numero`, `saldo`.

3. **ContaCorrente (subclasse de Conta)**
   - Implementa uma conta corrente com limite de saque diário.
   - Atributos: herda da classe Conta, adicionando `limite_saque_diario` e controle de número de saques.

4. **Transacao (classe abstrata)**
   - Representa uma transação financeira. É a base para operações de depósito e saque.

5. **Banco**
   - Gerencia os clientes e contas do banco. Essa classe mantém o registro de todos os usuários e suas respectivas contas, permitindo realizar as operações bancárias.
   - Métodos: `adicionar_cliente()`, `criar_conta()`, `realizar_saque()`, `realizar_deposito()`, `exibir_extrato()`, `listar_contas()`.

### Fluxo de Funcionamento

O sistema segue um fluxo simples, onde os clientes e suas contas são registrados primeiro. Após isso, o cliente pode realizar operações como depósito, saque e consulta de extrato.

1. **Criar um cliente**: O cliente é criado com os atributos necessários e é adicionado ao sistema.
   
2. **Criar uma conta**: Uma ou mais contas podem ser associadas a um cliente existente.

3. **Realizar transações**: O cliente pode realizar depósitos e saques em suas contas, sempre com validações de saldo e limites.

4. **Consultar extrato**: O histórico de transações é exibido para o cliente de acordo com as contas selecionadas.

### Diagrama Simplificado de Classes

```plaintext
+------------------+
|      Cliente      |
+------------------+
| nome             |
| cpf              |
| data_nascimento  |
| endereco         |
+------------------+
        |
        |
+-------------------+
|      Conta        | (abstract)
+-------------------+
| agencia           |
| numero            |
| saldo             |
+-------------------+
        ^
        |
+---------------------+
|    ContaCorrente    |
+---------------------+
| limite_saque_diario |
| num_saques          |
+---------------------+
        |
+-------------------+
|    Banco          |
+-------------------+
| clientes          |
| contas            |
+-------------------+
```

## Requisitos

- **Python 3.6+**
  
## Instalação e Execução

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/agabilobbo/banco_poo.git
   ```

2. **Navegue até o diretório do projeto**:
   ```bash
   cd banco_poo
   ```

3. **Execute o arquivo principal**:
   ```bash
   python main.py
   ```

Aqui está a seção "Uso" reformulada em formato de tabela:

---

### Uso

| **Operação**           | **Descrição**                                                                                                       | **Passos**                                                                                                                                         |
|------------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| **Criar um Cliente**    | Cria um novo cliente no sistema com nome, CPF e data de nascimento.                                                  | No menu, selecione a opção para criar cliente e insira as informações solicitadas.                                                                 |
| **Criar uma Conta**     | Associa uma nova conta bancária a um cliente existente.                                                             | Após criar o cliente, escolha a opção para criar conta e insira os dados da agência e número da conta.                                             |
| **Realizar um Depósito**| Permite depositar uma quantia em uma conta existente.                                                               | No menu, selecione "Depósito", escolha a conta e insira o valor a ser depositado.                                                                  |
| **Realizar um Saque**   | Realiza o saque de uma quantia, desde que o saldo e o limite diário de saques permitam.                             | Selecione "Saque", escolha a conta, insira o valor e o sistema validará as condições para o saque.                                                 |
| **Consultar Extrato**   | Exibe o histórico de transações (depósitos e saques) de uma conta específica.                                       | Escolha a opção de "Extrato" no menu, selecione a conta desejada para visualizar o histórico de transações.                                        |
| **Listar Contas**       | Lista todas as contas registradas no sistema, exibindo detalhes como agência, número da conta e saldo atual.        | No menu, selecione "Listar Contas" para visualizar as contas cadastradas no banco.                                                                 |

## Melhorias Futuras

- Adicionar integração com um banco de dados para persistência de dados.
- Implementar autenticação de usuários.
- Expandir funcionalidades, como transferências entre contas.
- Melhorar interface de usuário com um frontend gráfico ou via API REST.

## Contribuições

Contribuições são sempre bem-vindas. Para contribuir, siga os seguintes passos:

1. Faça um fork do projeto.
2. Crie uma nova branch com suas alterações.
3. Submeta um pull request explicando as mudanças.

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Esse README fornece uma visão detalhada do sistema bancário POO, explicando suas funcionalidades, estrutura e como usá-lo.