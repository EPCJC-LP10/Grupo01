# -*- coding: iso8859-1 -*-

def principal():
    print
    print " **** MENU ****** "
    print
    print "   1. Gestão de Eventos"
    print "   2. Gestão de noites "
    print 
    print "   0. Sair"
    print 

    op = raw_input("Opção: ")
    return op


def eventos():
    print
    print " *** Menu Eventos **** "
    print
    print "1. Inserir novo eventos"
    print "2. Listar todos eventos"
    print "3. Pesquisar eventos"
    print "4. Alterar dados de um evento"
    print "5. Eliminar evento"
    print 
    print "0. Menu Anterior"

    op = raw_input("Opção: ")
    return op


def noite():
    print
    print " *** Menu Noite **** "
    print
    print "1. Inserir nova noite"
    print "2. Listar todas as noites"
    print "3. Pesquisar noites"
    print "4. Alterar dados de uma noite"
    print "5. Eliminar noite"
    print 
    print "0. Menu Anterior"

    op = raw_input("Opção: ")
    return op



if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"

