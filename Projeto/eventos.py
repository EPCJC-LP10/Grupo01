# -*- coding: utf-8 -*-

# Programa feito por Manel e Zé

from collections import namedtuple

import menu



eventoReg = namedtuple("EventoReg", "id, nome, tipo, hhii, hhff, custo")
ListaEventos = []



def encontrar_posicao(codigo):
    pos = -1
    for i in range (len(ListaEventos)):
        if ListaEventos[i].id == codigo:
            pos = i
            break
                            
    return pos


def inserir_evento():
    cod = input("Qual o codigo? ")

    pos = encontrar_posicao(cod)

    if pos >= 0:
        print "Código já existe"
        return

    #ler dados
    nome = raw_input("Qual o nome? ")
    tipo = raw_input("Qual o tipo de evento?")
    hhii= raw_input ("Qual a hora de inicio?")
    hhff= raw_input ("Qual a hora de fim?")
    custo= raw_input ("Qual o custo final?")
    
    registo = eventoReg(cod, nome,tipo,hhii,hhff,custo)
    ListaEventos.append(registo)


def pesquisar_evento():
    cod = input("Qual o codigo do evento a pesquisar? ")

    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe evento com esse código"
        return

    print "Código: ", ListaEventos[pos].id
    print "Nome: ", ListaEventos[pos].nome
    print "tipo de evento", ListaEventos[pos].tipo
    print "hora de inicio", ListaEventos[pos].hhii
    print "hora do fim", ListaEventos[pos].hhff
    print "custo do evento", ListaEventos[pos].custo
def listar_evento():
    for i in range (len(ListaEventos)):
        print "Código: ", ListaEventos[i].id
        print "Nome: ", ListaEventos[i].nome
        print "tipo de evento", ListaEventos[i].tipo
        print "hora de inicio", ListaEventos[i].hhii
        print "hora de fim", ListaEventos[i].hhff
        print "custo de evento", ListaEventos[i].custo
        
  

def eliminar_evento():
    cod = input ("Código do evento a eliminar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe evento com esse código"
        return

    # TODO: Confirmar eliminação
    ListaEventos.pop(pos)


    
def alterar_evento():
    cod = input ("Código do evento a alterar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe evento com esse código"
        return

    # só altera o nome
    novonome = raw_input("Qual o nome? ")
    ListaEventos[pos] = ListaEventos[pos]._replace(nome=novonome)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.eventos()

        if op == '1':
            inserir_evento()
        elif op =='2':
            listar_evento()
        elif op == '3':
            pesquisar_evento()
        elif op == '4':
            alterar_evento()
        elif op == '5':
            eliminar_evento()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente3aa"










