#from ast import main
import os
from operacoes import*

if __name__ == "__main__":

    conta = None
    while True:
            menu()
            opcao = input('Informe a opção desejada: ')
            os.system('cls')
        
            match opcao:
            
                case '1':
                    if  conta is None:
                        conta = criar_conta()
                        print('A conta foi criada com sucesso.')
                        continue
       
                case '2':
                    if  conta is not None:
                        conta.exibir_dados()
                        continue
                
                case '3':
                    if  conta is not None:
                        valor = float(input('Informe o valor a ser depositado: '))
                        conta.depositar(valor)
                        continue   
                
                case '4':
                    if  conta is not None:
                        valor = float(input('Informe o valor a ser sacado: '))
                        conta.sacar(valor)
                        continue

                case '5':
                    if  conta is not None:
                        conta.encerrar_conta()
                        conta = None
                        print('Conta encerrada com sucesso')
                        continue
                case '6':
                        print('Sistema bancário encerrado com sucesso.')
                        break
             

      
