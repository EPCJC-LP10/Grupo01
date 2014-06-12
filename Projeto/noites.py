# -*- coding: iso8859-1 -*-
"""
Created on Fri Jun 06 12:25:38 2014

@author: i13311
"""

from collections import namedtuple

import menu


noiteReg = namedtuple("noiteReg", "id, Data, numero de entradas,clientes registados, faturacao, totalMaterias, totalFuncionarios")
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
    clientesregistados= raw_input ("Quais os clientes registados?")
    faturacao= raw_input ("Qual a fatura�ao?")
    totalgastomaterial= raw_input ("Qual o gasto do material?")
    totalgastofuncionarios= raw_input("qual o gasto em funcionarios")
    registo = noiteReg(cod, data,numeroentradas,clientesregistados,faturacao,totalgastomaterial,totalgastofuncionarios)
    Listanoite.append(registo)


def pesquisar_noite():
    cod = input("Qual o codigo da noite? ")

    pos = encontrar_posicao(cod)

    if pos == -1:
        print "N�o existe noite com esse c�digo"
        return

    print "C�digo: ", Listanoite[pos].id
    print "Data: ", 
    print Listanoite[pos].data.dia, "/", Listanoite[pos].data.mes, "/",
    print Listanoite[pos].data.ano
    print "numero de entradas", Listanoite[pos].numeroentradas
    print "clientes registados", Listanoite[pos].clientesregistados
    print "fatura��o", Listanoite[pos].faturacao
    print "total gasto em material", Listanoite[pos].totalgastomaterial
    print "total gasto em funcionarios", Listanoite[pos].totalgastofuncionarios
    
def listar_noite():
    for i in range (len(Listanoite)):
        print "="*50
        print "C�digo: ", Listanoite[i].id
        print "Data: ", 
        print Listanoite[i].data.dia, "/", Listanoite[i].data.mes, "/",
        print Listanoite[i].data.ano
        print "N�mero de entradas", Listanoite[i].numeroentradas
        print "Hora inicio: ", Listanoite[i].clientesregistados
        print "hora de fim", Listanoite[i].faturacao
        print "custo de noite", Listanoite[i].totalgastomaterial
        print "custo de noite", Listanoite[i].totalgastofuncionarios
  

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

    # s� altera o nome
    novadata = raw_input("Qual a data? ")
    Listanoite[pos] = Listanoite[pos]._replace(nome=novadata)



        

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
