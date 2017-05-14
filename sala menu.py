

def imprimir_sala(salas):
    print('Cod. Sala: ',salas[0])
    print('Capacidade: ', salas[1])
    
def criar():
    cod_sala = int(input('Digite o código da sala: '))
    capacidade = int(input('Digite a capacidade :'))
    sala.criar_sala(cod_sala,capacidade)

def obter():
    cod_sala= int(input('Obter sala pelo código de sala: '))
    o = sala.obter_sala(cod_sala)
    if o==None:
        print('Sala não encontrada! ')
    else:
        imprimir_sala(o)

def listar():
    print(' Listar salas \n')
    salas = sala.listar_salas()
    for s in salas:
        imprimir_sala(s)

def excluir():
    print('\n Excluir sala')
    cod_sala = int(input('Cod. Sala: '))
    s = sala.excluir_sala(cod_sala)
    if (s == False):
        print ("Sala não encontrada")
    else:
        print ("Sala excluida")
    
def alterar():
    print('\n Alterar sala')
    cod_sala = int(input('Cod. Sala: '))
    s = sala.listar_salas()
    if (s == False):
        print ("Sala não encontrada")
    else:
        capacidade = int(input('Digite a nova capacidade da sala: '))
        s = sala.obter_sala(cod_sala)
        s[1] = capacidade
        sala.alterar_sala(cod_sala,capacidade)
        return capacidade

def excluirTodas():
    sala.remover_todas_as_salas()
    
        
def mostrar():
    run_sala = True
    menu = ("\n----------------\n"+
             "(1) Criar sala \n" +
             "(2) Listar salas \n" +
             "(3) Obter sala por Cód. Sala \n" +
             "(4) Excluir sala \n" +
             "(5) Alterar sala \n"+
             "(6) Remover TODAS as salas \n"+
             "(0) Voltar\n"+
            "----------------")
    
    while(run_sala):
        print (menu)
        op = int(input("Digite sua escolha: "))

        if op == 1:
            criar()
        elif op == 2:
            listar()
        elif op == 3:       
            obter()
        elif op == 4:
            excluir()
        elif op == 5:
            alterar()
        elif op == 6:
            excluirTodas()
        elif op ==7:
            criar()
        elif op == 0:
            run_sala = False

if __name__ == "__main__":
    menu_mostrar()
        
    
