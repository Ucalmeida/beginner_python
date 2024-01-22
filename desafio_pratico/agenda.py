def adicionar_contato(contatos, nome_contato, telefone_contato, email_contato):
    contato = {'nome': nome_contato, 'telefone': telefone_contato, 'email': email_contato, 'favorito': False}
    contatos.append(contato)
    print(f'O contato\nNome: {nome_contato}\nTelefone: {telefone_contato}\nEmail: {email_contato}\nfoi adicionada com '
          'sucesso!')
    return


def ver_tarefas(tarefas):
    print('\nLista de Tarefas:')
    for indice, tarefa in enumerate(tarefas, start=1):
        status = '\u2713' if tarefa["completada"] else ' '
        nome_tarefa_adicionada = tarefa['nome']
        print(f'{indice}. [{status}] {nome_tarefa_adicionada}')


def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    if 0 <= indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]['nome'] = novo_nome_tarefa
        print(f'Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}')
    else:
        print('Índice de Tarefa inválido!')
    return


def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    tarefas[indice_tarefa_ajustado]['completada'] = True
    print(f'Tarefa {indice_tarefa} marcada como completada!')
    return


def deletar_tarefas_completadas(tarefas):
    for tarefa in tarefas:
        if tarefa['completada']:
            tarefas.remove(tarefa)
    print('Tarefas completadas foram deletadas \u274c')
    return


contatos = []

while True:
    print('\nMenu da Agenda:')
    print('1 - Adicionar contato à Agenda')
    print('2 - Ver Contatos da Agenda')
    print('3 - Atualizar Contatos da Agenda')
    print('4 - Marcar/Desmarcar como Favorito')
    print('5 - Ver Contatos Favoritos')
    print('6 - Apagar Contato da Agenda')
    print('7 - Sair')

    escolha = input('Escolha uma opção: ')

    if escolha == "1":
        nome_contato = input('Digite o nome do Contato que deseja Adicionar: ')
        telefone_contato = input('Digite o telefone do Contato que deseja Adicionar: ')
        email_contato = input('Digite o email do Contato que deseja Adicionar: ')
        adicionar_contato(contatos, nome_contato, telefone_contato, email_contato)
    elif escolha == "2":
        pass # ver_tarefas(tarefas)
    elif escolha == "3":
        # ver_tarefas(tarefas)
        indice_tarefa = input('Digite o número da Tarefa que deseja atualizar: ')
        novo_nome = input('Digite o novo nome da Tarefa: ')
        # atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)
    elif escolha == "4":
        # ver_tarefas(tarefas)
        indice_tarefa = input('Digite o número da Tarefa que deseja completar: ')
        # completar_tarefa(tarefas, indice_tarefa)
    elif escolha == "5":
        pass # deletar_tarefas_completadas(tarefas) ver_tarefas(tarefas)
    elif escolha == "6":
        pass
    elif escolha == "7":
        break

print('Programa Finalizado')
