sessões = []
import sala
import filme

def sessao(cod_sessao,cod_filme,cod_sala,horario,capacidade):
    sessao = [cod_sessao,cod_filme, cod_sala, horario,capacidade]
    sessoes.append(sessao)
    
def sessoes(cod_sessao, cod_filme, cod_sala, horario, capacidade):
    for a in sessoes:
        if a[0] == cod_sessao:
            a[1] = cod_filme
            a[2] = cod_sala
            a[3] = horario
            a[4] = capacidade
            return True
        return False
    
def sessao(cod_sessao):
    for s in sessoes:
        if s[0] == cod_sessao:
            return s
        
def disponibilidade(cod_sessao):
    s= buscar_sessao(cod_sessao)
    return s
    
def sessao(cod_sessao):
    for s in sessoes:
        if s[0] ==cod_sessao:
            sessoes.remove(s)
            return True
        return False
def sessao():
    return sessoes
def remover_sessoes():
    global sessoes
    sessoes=[]
