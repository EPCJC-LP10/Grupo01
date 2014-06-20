# -*- coding: iso8859-1 -*-

import menu
import eventos
import util
import noites


# nome dos ficheiros
fxEventos = "fxEventos.dat"
fxNoites= "fxNoites"

def ler_ficheiros():
    # adicionar todos ficheiros a ler
    eventos.Listaeventos = util.ler_ficheiro(fxEventos)
    noites.Listanoite = util.ler_ficheiro(fxNoites)


def escrever_ficheiros():
    # adicionar todos ficheiros a guardar
    util.escrever_ficheiro(fxEventos, eventos.Listaeventos)
    util.escrever_ficheiro(fxNoites, noites.Listanoite)



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


