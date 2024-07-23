import os

restaurantes = [{'nome': 'son sushi', 'categoria':'sushi', 'ativo':True},
                {'nome': 'good pizza', 'categoria': 'pizza', 'ativo': False},
                {'nome': 'good burguer', 'categoria': 'hambúrguer', 'ativo': True},
]

def exibir_titulo():
    print('Sabor Express\n')

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print(' ')

def voltar():
    input('\nDigite uma tecla caso deseje voltar para o menu principal: ')
    main()

def exibir_opcoes():
    print('1. Cadastrar Restautante: ')
    print('2. Listar Restautante: ')
    print('3. Ativar Restautante: ')
    print('4. Sair\n')

def cadastrar_restaurantes():
    exibir_subtitulo('Cadastro de novos restaurantes:\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome':nome_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
    voltar()

def mostrar_restaurantes():
    exibir_subtitulo('Lista de restaurantes:')
    for item in restaurantes:
        nome_restarante = item['nome']
        categoria = item['categoria']
        ativo = item['ativo']
        print(f'- {nome_restarante} | {categoria} | {ativo}.')
    voltar()

def trocar_estado_restaurante():
    exibir_subtitulo()
    nome_restaurante = input('Digite o nome do restaurante que deseja ativar ou desativar: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante}foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print('Restaurante não encontrado.')

    voltar()

def encerrar_app():
    exibir_subtitulo('Programa encerrado.')

def opcao_invalida():
    print('Opção inválida!\n')
    input('Digite uma tecla para voltar ao começo:')
    main()

def escolher_opcoes():

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_restaurantes()
        elif opcao_escolhida == 2:
            mostrar_restaurantes()
        elif opcao_escolhida == 3:
            trocar_estado_restaurante()
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