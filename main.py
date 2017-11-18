# -*- coding: utf-8 -*-

#       === SMART SCHOOL ===
#   JOGO DA VELHA COM PYTHON v1.0.0 
#        www.smartweb.co.ao

# Libs do Python

import random, os

#======================== VARIAVEIS GLOBAIS

limpa	= "os.system('cls' if os.name == 'nt' else 'clear')"
jogando = 'X'
X		= 0
O 		= 0
em 		= 0
V 		= [

	[1,2,3],
	[4,5,6],
	[7,8,9]

]

# ========================= INTERFACE =========================

def cabecalho():
	print("|=====================================================|")
	print("|              JOGO DA VELHA COM PYTHON               |")
	print("|=====================================================|")

def placar():
	print("|                       PLACAR                        |")
	print("|     ( O ) => 3                      3 <= ( X )      |")
	print("|     EMPATES => 2                                    |")
	print("|=====================================================|")
	print("|                    Jogando =>  X                    |")	 
	print("|=====================================================|")	 

def velha():
	print("|                 +-----+-----+-----+                 |")
	print("|                 |  1  |  2  |  3  |                 |")
	print("|                 +-----+-----+-----+                 |")
	print("|                 |  4  |  5  |  6  |                 |")
	print("|                 +-----+-----+-----+                 |")
	print("|                 |  7  |  8  |  9  |                 |")
	print("|                 +-----+-----+-----+                 |")
	print("|-----------------------------------------------------|")

# ========================= FUNCOES AUXILIARES =========================

def jogador(): # Escolha o jogador

	return 'X' if random.randint(1,2) == 1 else 'O'

def jogou(msg):

	while True:
		try:
			jogada = input(msg)
			return int(jogada[0])
		except:
			print("Sertifique-se de que digitou um valor aceite!")

def questao(msg, erro="Digite S para sim e N para não"):

	while True:
		try:
			r = input(msg)
			if( r[0] == 'S' or r[0] == 's' ):
				return True
			elif( r[0] == 'N' or r[0] == 'n' ):
				return False
			else:
				print(erro)
		except:
			print("Sertifique-se de que digitou um valor aceite!")

eval(limpa)

print(jogador())
print(jogou('Joga na pusicao: '))
print(questao("Quer jogar mais? "))

