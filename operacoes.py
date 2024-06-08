
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

    def depositar(self, valor):
            if valor > 0:
                self.saldo += valor
                print('Depósito de R$ {:.2f} realizado com sucesso.'.format(valor))
            else:
                print('Valor inválido.')

    def sacar(self, valor):
            if valor > 0 and self.saldo >= valor:
                self.saldo -= valor
                print('Saque de R$ {:.2f} realizado com sucesso.'.format(valor))
            else:
                print('Saldo insuficiente.')

    def exibir_dados(self):
            print('Nome: {}'.format(self.nome))
            print('CPF: {}'.format(self.cpf))
            print('Saldo: R$ {:.2f}'.format(self.saldo))

    def encerrar_conta(self):
            self.saldo = 0.0
            print('Conta encerrada.')

def criar_conta():
    nome = input('Informe seu nome completo: ')
    cpf = input('Informe o seu CPF: ')
    return conta_corrente(nome, cpf)



   