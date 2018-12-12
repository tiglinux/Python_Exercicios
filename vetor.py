# -*- coding: utf-8 -*-

# Desenvolver um programa que leia 20 num inteiros
# e armazene-os num vetor.Armazenar os num pares no vetor PAR
# e os num impar no vetor impar no vetor impar , imprimir os 3 vet

num = 0


def vetores():
    global num
    num = []
    par = []
    impar = []
    cont = 0
    
    while(cont < 3):
        num = (int)(input("Digite o %d numero:"%(cont+1)))
        if (num / 2 == 0):
            par.append(num)
            print("\n Os números pares são : ",par)
        else:
            if (num / 2 == 1):
                impar.append(num)
        cont+=1

    print(par)
    
      
#call the def vetores() function        
vetores()
