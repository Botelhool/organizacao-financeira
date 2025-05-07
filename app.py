
import os
def operacao (tipo,descricao, valor,transacoes): 
    transacao = {
        'tipo': tipo,
        'descrição': descricao,
        'valor' : valor    
    }

    transacoes.append (transacao)
    print(transacoes)

def verificar_operacoes(transacoes):
    
    print('Veirificando operações\n')
    resposta_user = int(input('Receitas (1) ou despesas (2): '))
    
    if resposta_user == 1:
        print('Receitas')
        for dic in transacoes:            
            if dic.get('tipo') == 'receitas' :
                print(dic)

    elif resposta_user == 2 :
        print('Despesas')
        for dic in transacoes:
            if dic.get('tipo') == 'despesas':
                print (dic)

    else:
        print('Valor inválido')


def clear ():
    return os.system('cls')

    
def main() :
    transacoes = [] 

    while True :
        print('\nMenu')
        print('opcao1: adicionar receita')
        print('opcao2 : adicionar despesas')
        print('opcao3 : verificar transacões')
        print('opcção4: sair\n')
        response_user = int(input('escolha uma opção: '))
        
        if response_user == 1 :
            clear ()
            print('\nopcao de receitas')
            valor= input('Digite o valor da receita:')
            descricao =input('Digite a descrição')
            operacao('receitas',descricao,valor,transacoes)

        elif response_user == 2:
            clear ()
            print('opcao de despesas')
           
            valor= input('Digite o valor da despesa:')
            descricao = input('Digite a descrição')
            operacao('despesas',descricao,valor,transacoes) 

        elif response_user == 3:
            clear()
            verificar_operacoes(transacoes)
        
        elif response_user == 4 :
            break

        else:
           print('Valor inválido, digite novamente')


        
main()