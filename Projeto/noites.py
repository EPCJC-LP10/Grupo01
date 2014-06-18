# -*- coding: iso8859-1 -*-
"""
Created on Fri Jun 06 12:25:38 2014

@author: i13311
"""

from collections import namedtuple

import menu


noiteReg = namedtuple("noiteReg", "id, Data, entradas, faturacao, totalMateriais, totalFuncionarios")
dataReg = namedtuple("dataReg", "dia, mes, ano")
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
        print "C�digo j� existe"
        return

    #ler dados
    print "Introduza data:"
    dia = input("\tDia:")
    mes = input("\tM�s:")
    ano = input("\tAno:")
    data = dataReg(dia, mes, ano)
    numeroentradas = raw_input("Qual o numero de entradas?")    
    faturacao= raw_input ("Qual a fatura�ao?")
    totalMateriais= raw_input ("Qual o gasto do material?")
    totalFuncionarios= raw_input("qual o gasto em funcionarios")
    registo = noiteReg(cod, data,numeroentradas,faturacao,totalMateriais,totalFuncionarios)
    Listanoite.append(registo)


def pesquisar_noite():
    cod = input("Qual o codigo da noite? ")

    pos = encontrar_posicao(cod)

    if pos == -1:
        print "N�o existe noite com esse c�digo"
        return

    print "C�digo: ", Listanoite[pos].id
    print "Data: ", 
    print Listanoite[pos].Data.dia, "/", Listanoite[pos].Data.mes, "/",
    print Listanoite[pos].Data.ano
    print "numero de entradas", Listanoite[pos].entradas
    print "fatura��o", Listanoite[pos].faturacao
    print "total gasto em material", Listanoite[pos].totalMateriais
    print "total gasto em funcionarios", Listanoite[pos].totalFuncionarios
    
def listar_noite():
    if len(Listanoite) == 0:
        print "N�o existem noites inseridas"
        return
        
    for i in range (len(Listanoite)):
        print "="*50
        print "C�digo: ", Listanoite[i].id
        print "Data: ", 
        print Listanoite[i].Data.dia, "/", Listanoite[i].Data.mes, "/",
        print Listanoite[i].Data.ano
        print "N�mero de entradas", Listanoite[i].entradas
        print "faturacao", Listanoite[i].faturacao
        print "totalgastomaterial", Listanoite[i].totalMateriais
        print "totalgastofuncionarios", Listanoite[i].totalFuncionarios
  

def eliminar_noite():
    cod = input ("C�digo de noite a eliminar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "N�o existe noite com esse c�digo"
        return

    # TODO: Confirmar elimina��o
    Listanoite.pop(pos)


    
def alterar_noite():
    cod = input ("C�digo da noite a alterar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "N�o existe noite com esse c�digo"
        return

    # alterar numero de entradas
    nova_entradas = raw_input("Qual o n�mero correto de entradas ")
    Listanoite[pos] = Listanoite[pos]._replace(entradas=nova_entradas)



        

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
    print "Este programa n�o deve ser executado diretamente3aa"
