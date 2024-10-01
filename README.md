# Sistema Bancário em Python
Este repositório contém dois sistemas bancários desenvolvidos em Python com diferentes níveis de complexidade, usando conceitos básicos e avançados da linguagem.

## Estrutura do Repositório
O repositório está organizado da seguinte forma:

- /sistema_bancario_basico: Contém o código para o sistema bancário com funcionalidades básicas, utilizando variáveis e condicionais.
- /sistema_bancario_avancado ou /banco_poo: Contém o código de um sistema bancário mais elaborado, implementado com Programação Orientada a Objetos (POO), herança e classes abstratas.

## Funcionalidades
### Sistema Bancário Básico
Este sistema bancário foi implementado utilizando uma estrutura simples com variáveis e condicionais. Ele permite executar as seguintes operações:

- Depósito: Permite adicionar valores ao saldo de uma conta.
- Saque: Permite realizar saques, verificando o saldo disponível e o número de saques permitidos.
- Exibir Extrato: Exibe todas as transações realizadas (depósitos e saques).
- Sair: Encerra o programa.

## Sistema Bancário Avançado (POO)
Este sistema bancário utiliza os conceitos de Programação Orientada a Objetos (POO), com classes abstratas e herança para um gerenciamento mais robusto de clientes e contas. As funcionalidades incluem:

- Criação de Usuários: Permite a criação de novos usuários com dados como nome, CPF e data de nascimento.
- Criação de Contas: Cria contas associadas a um usuário e gerencia múltiplas contas.
- Depósitos e Saques: Implementa depósitos e saques, validando condições como saldo e limite de saques diários.
- Consulta de Extrato: Exibe um histórico detalhado de transações (depósitos e saques).
- Listagem de Contas: Exibe todas as contas criadas no sistema.

## Requisitos
Para executar ambos os sistemas, você precisará ter o Python instalado em sua máquina. Certifique-se de ter uma versão superior à 3.6 para evitar problemas de compatibilidade.

### Instruções de Execução
1.Clone o repositório:

>>git clone https://github.com/agabilobbo/sistema-bancario.git

2.Navegue até o diretório correspondente:

- Para o sistema básico: **cd sistema_bancario_basico**
- Para o sistema avançado: **cd banco_poo**

3.Execute o arquivo Python:
>> python main.py

### Melhorias Futuras

_ Adicionar persistência de dados com banco de dados ou arquivos.
- Implementar interface gráfica ou API.
- Expandir as funcionalidades de transações e relatórios.

### Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir pull requests ou reportar problemas na seção de "Issues".