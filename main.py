# -*- coding: utf-8 -*-

#       === SMART SCHOOL ===
#   JOGO DA VELHA COM PYTHON v1.0.0 
#        www.smartweb.co.ao

# Libs do Python

import random, os, time

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
	print("|     ( O ) => "+str(O)+"                      "+str(X)+" <= ( X )      |")
	print("|     EMPATES => "+str(em)+"                                    |")
	print("|=====================================================|")
	print("|                    Jogando =>  "+str(jogando)+"                    |")	 
	print("|=====================================================|")	 

def velha():
	print("|                 +-----+-----+-----+                 |")
	print("|                 |  "+str(V[0][0])+"  |  "+str(V[0][1])+"  |  "+str(V[0][2])+"  |                 |")
	print("|                 +-----+-----+-----+                 |")
	print("|                 |  "+str(V[1][0])+"  |  "+str(V[1][1])+"  |  "+str(V[1][2])+"  |                 |")
	print("|                 +-----+-----+-----+                 |")
	print("|                 |  "+str(V[2][0])+"  |  "+str(V[2][1])+"  |  "+str(V[2][2])+"  |                 |")
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

# ========================== FUNCOES PRINCIPAIS =========================

def jogoEmpatado():

	for i in range(3):
		for j in range(3):
			if str(V[i][j]).isdigit():
				return False 

	return True

# =======================================================================

Inicio = True

while Inicio:

	jogando = jogador()
	GameOn  = True 

	while GameOn:

		# Cabecalho

		eval(limpa); cabecalho(); placar(); velha()

		jogada = jogou("| Jogue o número da posição que deseja: ")

		# Validacao

		jogadaAceite = False 

		for i in range(3):
			for j in range(3):
				if jogada == V[i][j]:
					V[i][j] = jogando 
					jogadaAceite = True

		if jogadaAceite:

			# Verificar se jogo foi ganho ou empate

			if jogoEmpatado():
				print("| Jogo empatado!... ")
				time.sleep(3)
				em += 1
				GameOn = False
				Inicio = True if questao("| Deseja continuar jogando? [N/S]: ") else False
			else:
				jogando = 'X' if jogando == 'O' else 'O'
		else:
			print("| Jogada invalida!... Tente outra vez.")
			time.sleep(3)

		if not questao("continua? "):


			GameOn = False 
			Inicio = False

