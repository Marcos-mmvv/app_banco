
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

def menu():
    print(f'{'-'*30} Escolha uma opção {'-'*30}\n')
    print('1. Criar conta')
    print('2. Exibir dados da conta')
    print('3. Depositar valor')
    print('4. Sacar valor')
    print('5. Encerrar conta')
    print('6. Sair do programa')

   