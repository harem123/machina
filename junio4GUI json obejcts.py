# falta agregar DB
# falta agregar preparar 
# falta agregar dificultad en relacion a TS
# se eleimono el caminar de las celdas 
#pruebas objetos 
import random
import time
import threading
import continuous_threading
import serial
import json 
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from tkinter import *
import tkinter as tk
import serial.tools.list_ports
# meter la funciones en una clase

class Machine(object):
	def __init__(self, _idSesion,_idUsuario):

		self.idSesion = _idSesion
		self.idUsuario = _idUsuario
		self.pwm1=100
		self.pwm2=100
		self.nVerde= (random.randrange(0,15))
		self.nAzul= (random.randrange(0,15))
		self.nWhite= (random.randrange(0,15))
		self.vector= [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
		self.blueAcumulate =0 
		self.redAcumulate =0
		self.greenAcumulate = 0
		self.greenCount = 0 
		self.redCount=0
		self.blueCount=0
		self.result=0
		self.ts = 3
		self.pared= (random.randrange(1,4))
		self.firstShooot = True
		self.shootCounter=4
		self.flagActiveSession=False
		self.shootFinished = False
		self.flagColor =0
		self.dificultad=1
		self.flagPreparar= True
		
	def creaCelda (self,verdeArg,azulArg,whiteArg):
		#falta guardar el valor de las celdas 
		
		if (verdeArg == 1):
			
			while (self.vector[self.nVerde] >= 1) :
					celdaActual = (random.randrange(0,15))
					if (self.vector[celdaActual]) > 0:
						self.nVerde = celdaActual
						self.vector[celdaActual] = 0
					if (celdaActual) < 15:
						self.vector[(celdaActual + 1)] = 0
					if (celdaActual) > 0:
						self.vector[(celdaActual - 1)] = 0

		if (azulArg == 1):
				
			if (self.vector[self.nAzul] >= 1) :
					self.vector[self.nAzul] = 0
			else: 
				while (self.vector[self.nAzul] == 0) :
					self.nAzul = (random.randrange(0,15))
					if (self.vector[self.nAzul] >= 1) :
						self.vector[self.nAzul] = 0

		if (whiteArg == 1):
				if (self.vector[self.nWhite] >= 1) :
					self.vector[self.nWhite] = 0
				else:
					while (self.vector[self.nWhite] == 0) :
						self.nWhite = (random.randrange(0,15))
						if (self.vector[self.nAzul] >= 1) :
							self.vector[self.nAzul] = 0

	def preparar(self):
	## ser = serial.Serial('COM' + str(port), baudrate=baud,timeout=1
		 #dataIn=  input('please enter shoot number ').strip('\n').strip('\r')
		self.shootCounter= int(shootCounterEntry.get())
		#self.shootCounter= int(dataIn)
		print(self.shootCounter)
		# falta insertar recibir comando de preparacion para sensores luces y motores 
		self.pared = (random.randrange(1,4))
		dataOut = '{"comd":0}'
		#self.shootCounter -= 1 
		print (dataOut)

	def getData(self):
				data = input('please enter json ').strip('\n').strip('\r')#{"comdA":3,"flagColor":3}
				j = json.loads(data)
				comd=j['comd']
				if comd == 3:
	                        ## if comdA es igual a 1 procedo sino no 
	                        ## ademas segun valor de flagColor tomo defino el valor 
	                        ## 1 verde 2 rojo 3 azul 4 blanco 
					self.flagColor= j['flagColor']
					print  (j['flagColor'])
					machine.shootFinished == True                     
	# se cambio la dinamica de tiros  el azul dura mas y el verde debe apagarse un poco antes y blanco por 3 tiros 
	def nuevoTiro(self):
			print ('{"comd":1,"cV":%d,"cA":%d,"cW":%d,"pwm1":%d,"pwm2":%d,"ss":%d,"ts":%d}'%(self.nVerde,self.nAzul,self.nWhite,200,200,1,10))
			self.shootCounter -= 1 
			self.firstShooot = False
			print('shot counter ',self.shootCounter)

	def writeDB(self):
		#if resultCounter <= 0: 
			#flagActiveSession = False 
			#mensaje_punTotal_aux.set(result)
			print('final ',self.result)
			print('writing BD ')
			time.sleep(3)

def salir():
    print("Salida inminente...!")
    exit()
## inicio flujo 
machine = Machine(100,1)


def main():

	while true 			
			input1 = int(input("ingrese 1 para iniciar "))
			print("aqui")
			if input1 == 1:
				## esto va a venir de tkinter
				machine.creaCelda(1,1,1)
				machine.flagActiveSession=True

				while machine.flagActiveSession:
					print("aqui2")
					if machine.flagPreparar:
						machine.preparar()
						machine.flagPreparar = False
						#print(shootCounter)
					## inicio de tiros y fin de preparar 
		
					if machine.shootCounter >= 1 and machine.shootFinished == True:
						machine.nuevoTiro()
						machine.firstShooot= True
						shootFinished == False

						#machine.shootCounter -= 1 

					if machine.firstShooot:
						machine.getData()

					if machine.flagColor == 3:

						blueCount = 1
						
						machine.blueAcumulate = machine.blueAcumulate + blueCount
						blueCount = 0
			
					if machine.flagColor == 2:

						redCount = 1
						machine.redAcumulate = machine.redAcumulate + redCount
						redCount = 0

					if machine.flagColor == 1:

						greenCount = 1	
						machine.greenAcumulate = machine.greenAcumulate + greenCount
						greenCount = 0

					machine.result= (machine.blueAcumulate*5) + (machine.redAcumulate * -5) + (machine.greenAcumulate * 10)

					print ("result",machine.result)
					print ("blue",machine.blueAcumulate)
					print ("red",machine.redAcumulate)
					print ("green",machine.greenAcumulate)
		
					if machine.shootCounter <=0:
						machine.writeDB()
						machine.flagActiveSession= False
						salir()
			

#t1 = threading.Thread(target = lops)
#t1.daemon = True
#t1.start()

if __name__ == '__main__':
    main();