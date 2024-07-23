import os

restaurantes = ['pizza', 'sushi']

def exibir_titulo():
    print('Sabor Express\n')

def exibir_opcoes():
    print('1. Cadastrar Restautante: ')
    print('2. Listar Restautante: ')
    print('3. Ativar Restautante: ')
    print('4. Sair\n')

def cadastrar_restaurantes():
    os.system('cls')
    print('Cadastro de novos restaurantes:\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
    input('Digite uma tecla caso deseje voltar para o menu principal: ')
    main()

def mostrar_restaurantes():
    os.system('cls')
    print('Lista de restaurantes cadastrados:\n') 
    for item in restaurantes:
        print(f'. {item}')

    input('Digite uma tecla caso deseje voltar para o menu principal: ')
    main()

def encerrar_app():
    os.system('cls')
    print('Programa encerrado. \n')

def opcao_invalida():
    print('Opção inválida!\n')
    input('Digite uma tecla para voltar ao começo:')
    main()

def escolher_opcoes():
    opcao_escolhida = 0

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_restaurantes()
        elif opcao_escolhida == 2:
            mostrar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurantes: ')
        elif opcao_escolhida == 4:
            encerrar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_titulo()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()