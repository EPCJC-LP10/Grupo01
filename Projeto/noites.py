# -*- coding: utf-8 -*-
"""
Created on Fri Jun 06 12:25:38 2014

@author: i13311
"""

from collections import namedtuple

import menu


noiteReg = namedtuple("noiteReg", "id, nome, tipo, hhii, hhff, custo")
Listanoite = []



def encontrar_posicao(codigo):
    pos = -1
    for i in range (len(Listanoite)):
        if Listanoite[i].id == codigo:
            pos = i
            break
                            
    return pos


def inserir_noite():
    cod = input("Qual o codigo? ")

    pos = encontrar_posicao(cod)

    if pos >= 0:
        print "Código já existe"
        return

    #ler dados
    nome = raw_input("Qual o nome? ")
    tipo = raw_input("Qual o tipo de noite?")
    hhii= raw_input ("Qual a hora de inicio?")
    hhff= raw_input ("Qual a hora de fim?")
    custo= raw_input ("Qual o custo final?")
    
    registo = noiteReg(cod, nome,tipo,hhii,hhff,custo)
    Listanoite.append(registo)


def pesquisar_noite():
    cod = input("Qual o codigo da noite? ")

    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe noite com esse código"
        return

    print "Código: ", Listanoite[pos].id
    print "Nome: ", Listanoite[pos].nome
    print "tipo de noite", Listanoite[pos].tipo
    print "hora de inicio", Listanoite[pos].hhii
    print "hora do fim", Listanoite[pos].hhff
    print "custo da noite", Listanoite[pos].custo
def listar_noite():
    for i in range (len(Listanoite)):
        print "Código: ", Listanoite[i].id
        print "Nome: ", Listanoite[i].nome
        print "tipo de noite", Listanoite[i].tipo
        print "hora de inicio", Listanoite[i].hhii
        print "hora de fim", Listanoite[i].hhff
        print "custo de noite", Listanoite[i].custo
        
  

def eliminar_noite():
    cod = input ("Código de noite a eliminar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe noite com esse código"
        return

    # TODO: Confirmar eliminação
    Listanoite.pop(pos)


    
def alterar_noite():
    cod = input ("Código da noite a alterar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe noite com esse código"
        return

    # só altera o nome
    novonome = raw_input("Qual o nome? ")
    Listanoite[pos] = Listanoite[pos]._replace(nome=novonome)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.noite()

        if op == '1':
            inserir_noite()
        elif op =='2':
            listar_noite()
        elif op == '3':
            pesquisar_noite()
        elif op == '4':
            alterar_noite()
        elif op == '5':
            eliminar_noite()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente3aa"
