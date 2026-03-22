lista = []

while True:
    print('\n1. Adicionar item à lista')
    print('2. Remover item da lista')
    print('3. Exibir lista de compras')
    print('4. Sair')

    try:
        e = int(input('Qual sua escolha: '))
    except:
        print('Digite um número válido!')
        continue

    if e == 1:
        item = input('Adicionar item à lista: ')
        lista.append(item)
        print('Item adicionado!')

    elif e == 2:
        item = input('Qual item deseja remover: ')
        if item in lista:
            lista.remove(item)
            print('Item removido!')
        else:
            print('Item não encontrado!')

    elif e == 3:
        if not lista:
            print('Lista vazia')
        else:
            print('Lista de compras:')
            for i in lista:
                print('-', i)

    elif e == 4:
        print('Saindo...')
        break

    else:
        print('Opção inválida!')