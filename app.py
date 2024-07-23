import os
def exibir_titulo():
    print('Sabor Express\n')

def exibir_opcoes():
    print('1. Cadastrar Restautante: ')
    print('2. Listar Restautante: ')
    print('3. Ativar Restautante: ')
    print('4. Sair\n')

def encerrar_app():
    os.system('cls')
    print('Programa encerrado. \n')



def escolher_opcoes():
    opcao_escolhida = 0

    while opcao_escolhida != 4:

        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            print('Cadastrar restaurantes: ')

        elif opcao_escolhida == 2:
            print('Listar restaurantes: ')

        elif opcao_escolhida == 3:
            print('Ativar restaurantes: ')

        else:
            encerrar_app()


def main():
    exibir_titulo()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()