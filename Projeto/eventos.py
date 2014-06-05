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
    cod = input("Qual o codigo do aluno a pesquisar? ")

    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe aluno com esse código"
        return

    print "Código: ", ListaEventos[pos].id
    print "Nome: ", ListaEventos[pos].nome
    print "tipo de evento", ListaEventos[pos].tipo
    


def listar_alunos():
    for i in range (len(ListaEventos)):
        print "Código: ", ListaEventos[i].id
        print "Nome: ", ListaEventos[i].nome
        
  

def eliminar_aluno():
    cod = input ("Código do aluno a eliminar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe aluno com esse código"
        return

    # TODO: Confirmar eliminação
    ListaEventos.pop(pos)


    
def alterar_aluno():
    cod = input ("Código do aluno a alterar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe aluno com esse código"
        return

    # só altera o nome
    novonome = raw_input("Qual o nome? ")
    ListaEventos[pos] = ListaEventos[pos]._replace(nome=novonome)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.alunos()

        if op == '1':
            inserir_aluno()
        elif op =='2':
            listar_alunos()
        elif op == '3':
            pesquisar_aluno()
        elif op == '4':
            alterar_aluno()
        elif op == '5':
            eliminar_aluno()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"










