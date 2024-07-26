import os

restaurantes = [{'nome': 'son sushi', 'categoria':'sushi', 'ativo':True},
                {'nome': 'good pizza', 'categoria': 'pizza', 'ativo': False},
                {'nome': 'good burguer', 'categoria': 'hambúrguer', 'ativo': True},
]

def exibir_titulo():
    print('Sabor Express\n')

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '-' * (len(texto))
    print(linha) 
    print(texto)
    print(linha)
    print(' ')

def voltar():
    input('\nDigite uma tecla caso deseje voltar para o menu principal: ')
    main()

def exibir_opcoes():
    print('1. Cadastrar Restaurante: ')
    print('2. Listar Restaurante: ')
    print('3. Ativar Restaurante: ')
    print('4. Sair\n')

def cadastrar_restaurantes():
    '''Cadastra novos restaurantes e os adiciona na biblioteca.
    
    input:
    - Nome do restaurante
    - categoria

    output:
    - Adiciona os dados do restaurante novo a biblioteca
    '''
    exibir_subtitulo('Cadastro de novos restaurantes:\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome':nome_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    voltar()

def mostrar_restaurantes():
    exibir_subtitulo('Lista de restaurantes:')

    print('Nome do restaurante:'.ljust(17), 'Categorias:'.ljust(19), 'Status:')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(17)} | {categoria.ljust(17)} | {ativo}.')
    voltar()



def encerrar_app():
    exibir_subtitulo('Programa encerrado.')

def opcao_invalida():
    print('Opção inválida!\n')
    input('Digite uma tecla para voltar ao começo:')
    main()

def trocar_estado_restaurante():
    '''Altera o estado dos restaurantes (True/False)
    
    input:
    - Nome do restaurante

    output:
    - Altera o valor do restaurante de True pra False ou vice-versa e informa ao usuário que foi trocado
    '''
    exibir_subtitulo('Alterando o estado do restaurante:')
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

def escolher_opcoes():
    '''Controle de escolha de opções do programa'''
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