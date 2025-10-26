import json


try:
    with open('arq.json', 'r') as arq:
        dados_do_arquivo = json.load(arq) # Lê o conteúdo do JSON
except FileNotFoundError:

    dados_do_arquivo = {
        "relatorio": {"Responsavel": "José", "Status_task": "pendente"},
        "reuniao_mensal": {"Responsavel": "Glaucia", "Status_task": "concluída"}
    }
except json.JSONDecodeError:
    print("Erro: O arquivo JSON está inválido. Usando dados iniciais.")
    dados_do_arquivo = {
        "relatorio": {"Responsavel": "José", "Status_task": "pendente"},
        "reuniao_mensal": {"Responsavel": "Glaucia", "Status_task": "concluída"}
    }


task_list = dados_do_arquivo

def print_list(task_list):

        print('LISTA DE TAREFAS')
        print(task_list)
        print('\n \n \n')
        edit=input('Deseja editar a lista de tarefas? \n').strip().lower()

        if edit=='sim':
            menu()


def menu():
        print('GERENCIADOR DE TAREFAS')
        print('1- Adicionar nova tarefa\n'
              '2- Mudar status de tarefa\n'
              '3- Mudar responsável de tarefa\n'
              '4- Retornar a pagina principal\n')
        print('\n \n ')
        edit=input('Digite o numero de sua escolha:\n ').strip().lower()

        if edit=='1':
            add_task()
        elif edit=='2':
            change_status_task(task_list)
        elif edit=='3':
            change_res_task(task_list)
        elif edit=='4':
            print_list(task_list)
        else:
            print('Entrada inválida! Tente novamente.')
            menu()

    #adiciona a tarefa a ser realizada
def add_task():
        global task_list
        task_name=input('Digite a tarefa:')
        task_task={}
        task_task['Responsavel']=input('Digite o responsável pela tarefa:')
        task_task['Status_task']=input('Digite o status da tarefa tarefa:')
        i=0
        while i<10:
            details=input('Deseja adicionar algum detalhe como hora, prioridade...? ')
            print('\n \n \n \n')
            if details == 'sim':
                name_detail=input('Digite o nome do detalhe: ')
                value_detail=input('Digite o valor do detalhe: ')
                task_task.update({name_detail:value_detail})
                i=i+1
            else:
                break
        task_list[task_name]=task_task
        salvar(task_list)
        print_list(task_list)
        return task_list

    #muda o status da tarefa
def change_status_task(task_list):
        task_change=input('Digite a tarefa que deseja modificar: ')
        if task_change in task_list:
            value_modifc=task_list[task_change]
            value_modifc["Status_task"]=input("Digite o novo status da tarefa: ")
            salvar(task_list)
            return task_list


    #muda o responsavel pela tarefa
def change_res_task(task_list):
        task_change=input('Digite a tarefa que deseja modificar:')
        if task_change in task_list:
            value_modifc=task_list[task_change]
            value_modifc["Responsavel"]=input("Digite o novo responsável tarefa: ")
            salvar(task_list)
            return task_list


def salvar(task_list):
    with open('arq.json', 'w', encoding='utf-8') as arq:
        json.dump(task_list, arq, indent=4, ensure_ascii=False)


while True:
        print_list(task_list)




