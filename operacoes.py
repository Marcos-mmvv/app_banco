# importa função de data
from datetime import date

<<<<<<< HEAD
# função exibir o menu
def exibir_menu():
    dia = date.today().day
    mes = date.today().month
    ano = date.today().year
=======
def cad():
     print(f'{'-'*30} Seja bem vindo ao app Senai Bank {'-'*30}')
     print('1 - Para acessar o APP')
     print('2 - Remover acesso ao APP')
     print()

def cadastro(entrada):
     entrada = entrada
     return entrada

def apagar(entrada):
     entrada = entrada.remove(entrada)

def menu():
    print(f'{'-'*30} APP Senai Bank {'-'*30}\n')
    print('1. Criar conta')
    print('2. Exibir dados da conta')
    print('3. Depositar valor')
    print('4. Sacar valor')
    print('5. Encerrar conta')
    print('6. Sair do programa')

class conta_corrente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0.0
>>>>>>> a1b78523630c33e7587c52ba99d9c3c06df0de9d

    print(f'\n{'=' * 20} | PYTHON BANK |  {'=' * 20}')
    print(f'\n{'=' * 23} {dia}/{mes}/{ano} {'=' * 25}\n')
    print('1 - Criar conta')
    print('2 - Entrar na conta')
    print('3 - Exibir correntistas')
    print('4 - Encerrar conta')
    print('5 - Encerrar programa')

# função exibir operações
def exibir_operacoes():
    print('\nOPERAÇÕES\n')
    print('1 - Consultar saldo')
    print('2 - Depositar valor')
    print('3 - Sacar valor')
    print('4 - Voltar')

# função exibir dados do correntista
def exibir_dados(nome, i, saldo):
    print(f'ID: {i}')
    print(f'Nome: {nome}')
    print(f'Agência: 1001')
    print(f'Conta: 1001{i}')
    print(f'Saldo: R$ {saldo}')

# função de depósito
def depositar_valor(saldo, valor):
    saldo += valor
    return saldo

<<<<<<< HEAD
# função de saque
def sacar_valor(saldo, valor):
    saldo -= valor
    return saldo
=======
def criar_conta():
    nome = input('Informe seu nome completo: ')
    cpf = input('Informe o seu CPF: ')
    return conta_corrente(nome, cpf)



   
>>>>>>> a1b78523630c33e7587c52ba99d9c3c06df0de9d
