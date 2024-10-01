# 🏦 Projeto de Sistema Bancário em Python

Este repositório contém **dois sistemas bancários** desenvolvidos em Python, abordando níveis distintos de complexidade. Eles foram implementados usando conceitos que variam desde programação básica até Programação Orientada a Objetos (POO).

## 📂 Estrutura do Repositório

- **📂 /sistema_bancario_basico**: Sistema simples utilizando variáveis e condicionais.
- **📂 /banco_poo**: Sistema mais avançado usando POO, com herança e classes abstratas.

## 🔑 Funcionalidades

### 🪙 Sistema Bancário Básico
O sistema bancário básico oferece operações essenciais com uma implementação simplificada. As principais funcionalidades são:

| Função            | Descrição                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------|
| 💰 **Depósito**    | Adiciona valor ao saldo da conta.                                                          |
| 🏧 **Saque**       | Retira dinheiro, verificando se o saldo é suficiente e respeitando o limite diário de saques. |
| 🧾 **Extrato**     | Mostra todas as transações (depósitos e saques) realizadas durante a sessão.               |
| 🚪 **Sair**        | Finaliza o programa.                                                                       |

### 🏦 Sistema Bancário Avançado (POO)
Este sistema é uma evolução do básico, utilizando Programação Orientada a Objetos para criar uma estrutura mais robusta. As funcionalidades incluem:

| Função                   | Descrição                                                                              |
|--------------------------|----------------------------------------------------------------------------------------|
| 👤 **Criação de Usuários**| Permite cadastrar novos usuários com nome, CPF e data de nascimento.                   |
| 🏦 **Criação de Contas**  | Associa uma ou mais contas ao usuário, gerenciando contas múltiplas.                    |
| 💰 **Depósitos e Saques** | Realiza transações financeiras com verificações de saldo e limites diários de saque.   |
| 🧾 **Consulta de Extrato**| Exibe um extrato detalhado das transações realizadas na conta.                         |
| 📋 **Listagem de Contas** | Mostra todas as contas criadas no sistema e seus detalhes.                             |

## 🔧 Requisitos

Certifique-se de ter o **Python 3.6+** instalado na sua máquina antes de executar os sistemas.

## ▶️ Como Executar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/agabilobbo/sistema-bancario.git
   ```

2. **Acesse o diretório**:
   - Para o sistema básico: `cd sistema_bancario_basico`
   - Para o sistema avançado: `cd sistema_bancario_avancado` ou `cd banco_poo`

3. **Execute o programa**:
   ```bash
   python main.py
   ```

## 🔮 Melhorias Futuras

- 💾 **Persistência de Dados**: Implementar salvamento de dados usando bancos de dados ou arquivos.
- 🎨 **Interface Gráfica**: Adicionar uma interface gráfica (GUI) para facilitar o uso.
- 📊 **Relatórios Avançados**: Incluir relatórios financeiros detalhados e gráficos para análise de transações.

## 💡 Contribuições

Contribuições são sempre bem-vindas! Abra uma **issue** para relatar bugs ou faça um **pull request** com suas melhorias. Vamos construir juntos!
