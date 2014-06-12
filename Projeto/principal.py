# -*- coding: iso8859-1 -*-

import menu
import eventos
import util
import noites


# nome dos ficheiros
fxEventos = "fxEventos.dat"

def ler_ficheiros():
    # adicionar todos ficheiros a ler
    eventos.Listaeventos = util.ler_ficheiro(fxEventos)


def escrever_ficheiros():
    # adicionar todos ficheiros a guardar
    util.escrever_ficheiro(fxEventos, eventos.Listaeventos)



# Bloco Principal

ler_ficheiros()

terminar = False
while not terminar:
    op = menu.principal()
    
    if op == '1':
        eventos.gerir()
    elif op == '2':
        noites.gerir()
    elif op == '0':
        terminar = True


escrever_ficheiros()


