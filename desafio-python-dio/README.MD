# Desafio DIO () 

Código fornecido pela DIO para o desafio do módulo proposto

## Otimizando o Sistema Bancário com Funções Python

Este projeto é um sistema bancário simples desenvolvido em Python. O sistema permite a criação de clientes, gerenciamento de contas, realização de transações como depósitos e saques, e exibição de extratos.

## Funcionalidades

- **Gerenciamento de Clientes**: Criação de novos clientes e busca de clientes existentes pelo CPF.
- **Gerenciamento de Contas**: Criação de contas correntes associadas a clientes.
- **Transações**: Realização de depósitos e saques, com controle de limites.
- **Extrato**: Visualização do extrato de transações realizadas em uma conta.
- **Registro de Transações**: Todas as transações realizadas são registradas com data e tipo.

## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte forma:

/sistema_bancario │ ├── main.py # Arquivo principal para execução do sistema ├── cliente.py # Definições das classes Cliente e PessoaFisica ├── conta.py # Definições das classes Conta e ContaCorrente ├── transacao.py # Definições das classes Transacao, Saque e Deposito ├── historico.py # Classe para gerenciar o histórico de transações └── utils.py # Funções utilitárias como menu e filtro de clientes

## Requisitos

Para executar este projeto, você precisará do Python 3.x instalado em sua máquina. Nenhum pacote adicional é necessário, pois todas as bibliotecas utilizadas são parte da biblioteca padrão do Python.

## Como Executar

1. Clone o repositório:
   ```bash
      git clone https://github.com/agabilobbo/sistema_bancario.git
   cd sistema_bancario

## Exemplo de Uso

1. Criar um cliente:

> O sistema solicitará o CPF, nome completo, data de nascimento e endereço.

2. Criar uma conta:

> Após a criação do cliente, você pode criar uma conta corrente para ele.

3. Realizar transações:

> Você pode depositar ou sacar valores da conta criada.

4. Exibir extrato:

> Visualize todas as transações realizadas em uma conta específica.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request ou relatar problemas.
