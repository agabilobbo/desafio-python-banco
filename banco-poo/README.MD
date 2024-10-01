# 🏦 Sistema Bancário com POO

Este projeto implementa um sistema bancário em Python utilizando conceitos avançados de **Programação Orientada a Objetos (POO)**. O sistema foi desenvolvido para fornecer um gerenciamento eficiente de clientes e contas bancárias, permitindo operações bancárias comuns, como depósito, saque e consulta de extrato.

---

## 🚀 Funcionalidades

| **Funcionalidade**               | **Descrição**                                                                                                                                      |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| 👤 **Criação de Usuários**       | Usuários podem ser criados no sistema com informações como nome, CPF e data de nascimento.                                                        |
| 🏦 **Criação de Contas**         | Contas podem ser criadas associadas a usuários com atributos como agência, número da conta e saldo inicial.                                       |
| 💰 **Depósitos**                 | Realiza depósitos em uma conta bancária, aumentando o saldo disponível.                                                                           |
| 🏧 **Saques**                    | Permite saques, respeitando o saldo e o limite diário de saques.                                                                                 |
| 📈 **Consulta de Extrato**       | Exibe o histórico completo de transações (depósitos e saques) de uma conta específica.                                                           |
| 📋 **Listagem de Contas**        | Exibe todas as contas registradas no sistema, mostrando detalhes como agência, número da conta e saldo atual.                                    |

---

## 🗂️ Estrutura do Projeto

O projeto está organizado em módulos e classes para separar responsabilidades e facilitar a manutenção do código.

### 🏗️ Classes Principais

| **Classe**                       | **Descrição**                                                                                      | **Atributos**                       |
|----------------------------------|--------------------------------------------------------------------------------------------------|-------------------------------------|
| **Cliente**                      | Representa um cliente do banco.                                                                   | `nome`, `cpf`, `data_nascimento`, `endereco` |
| **Conta (classe abstrata)**     | Representa uma conta bancária, definindo atributos e comportamentos básicos.                      | `agencia`, `numero`, `saldo`        |
| **ContaCorrente**               | Implementa uma conta corrente com limite de saque diário.                                        | `limite_saque_diario`, `num_saques` |
| **Transacao (classe abstrata)** | Representa uma transação financeira, base para operações de depósito e saque.                     | N/A                                 |
| **Banco**                       | Gerencia os clientes e contas, mantendo o registro de usuários e contas.                        | `clientes`, `contas`               |

---

### 🔄 Fluxo de Funcionamento

| **Passo**                        | **Descrição**                                                                                      |
|----------------------------------|--------------------------------------------------------------------------------------------------|
| 1. **Criar um cliente**          | O cliente é criado com os atributos necessários e adicionado ao sistema.                        |
| 2. **Criar uma conta**           | Uma ou mais contas podem ser associadas a um cliente existente.                                  |
| 3. **Realizar transações**       | O cliente pode realizar depósitos e saques em suas contas, sempre com validações de saldo.      |
| 4. **Consultar extrato**         | O histórico de transações é exibido para o cliente de acordo com as contas selecionadas.       |

---

### 📊 Diagrama Simplificado de Classes

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

---

## 🛠️ Requisitos

| **Requisitos**            | **Descrição**                  |
|---------------------------|--------------------------------|
| **Python 3.6+**          | O sistema foi desenvolvido para rodar em Python 3.6 ou superior. |

---

## 📥 Instalação e Execução

| **Passo**                          | **Comando**                                     |
|------------------------------------|-------------------------------------------------|
| 1. **Clone o repositório**        | ```bash git clone https://github.com/agabilobbo/banco_poo.git ``` |
| 2. **Navegue até o diretório**    | ```bash cd banco_poo ```                        |
| 3. **Execute o arquivo principal** | ```bash python main.py ```                      |

---

## 📋 Uso

| **Operação**                     | **Descrição**                                                                                          |
|----------------------------------|--------------------------------------------------------------------------------------------------------|
| 👤 **Criar um cliente**           | No menu interativo, siga as instruções para criar um cliente fornecendo nome, CPF e data de nascimento. |
| 🏦 **Criar uma conta**            | Após criar um cliente, crie uma conta associada ao cliente informando os detalhes da conta.            |
| 💰 **Realizar um depósito**       | Selecione a opção de depósito no menu, escolha a conta desejada e insira o valor a ser depositado.     |
| 🏧 **Realizar um saque**          | Selecione a opção de saque no menu, escolha a conta e insira o valor desejado. O sistema verificará o saldo e o limite de saques. |
| 📈 **Consultar extrato**          | Para visualizar o histórico de transações, escolha a opção de extrato no menu.                        |
| 📋 **Listar contas**              | Você pode visualizar todas as contas registradas no sistema selecionando a opção de listagem.          |

---

## 🔮 Melhorias Futuras

| **Melhoria**                                           | **Descrição**                                                 |
|-------------------------------------------------------|---------------------------------------------------------------|
| 🔗 **Integração com banco de dados**                  | Adicionar suporte para persistência de dados.                 |
| 🔒 **Implementar autenticação de usuários**            | Garantir a segurança das contas com login.                    |
| 🔄 **Expandir funcionalidades**                        | Adicionar transferências entre contas e outras operações.     |
| 🎨 **Melhorar interface de usuário**                   | Criar um frontend gráfico ou via API REST.                    |

---

## 🤝 Contribuições

Contribuições são sempre bem-vindas! Para contribuir, siga os seguintes passos:

1. Faça um fork do projeto.
2. Crie uma nova branch com suas alterações.
3. Submeta um pull request explicando as mudanças.

---

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

