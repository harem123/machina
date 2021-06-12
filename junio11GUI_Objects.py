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
		self.flagPreparar= False
		self.detener = False
		self.flagIniciar = False
		
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
		self.shootCounter= int(tiros_entry.get())
		self.ts= int(tiempoc_entry.get())
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
			print ('{"comd":1,"cV":%d,"cA":%d,"cW":%d,"pwm1":%d,"pwm2":%d,"ss":%d,"ts":%d}'%(self.nVerde,self.nAzul,self.nWhite,200,200,1,self.ts))
			self.shootCounter -= 1 
			self.firstShooot = False
			print('shot counter ',self.shootCounter)

	def writeDB(self):
		#if resultCounter <= 0: 
			#flagActiveSession = False 
			#mensaje_punTotal_aux.set(result)
			print('final ',self.result)
			lblpuntT.config(text= self.result)
			print('writing BD ')
			time.sleep(3)

def salir():
    print("Salida inminente...!")
    exit()

def dentention():
	machine.detener = True
	print ('{"comd":x,pwm1":0,"pwm2":0}')

def iniciar():
	machine.flagActiveSession = True
	print("iniciando")

def prepFunction():
	flagPreparar= True
	print("preparando")
## inicio flujo 




def mainloop():

	while machine.detener == False: 			
			#input1 = int(input("ingrese 1 para iniciar "))
			
			
			print("celda creada")
				#machine.flagActiveSession=True
			if machine.flagPreparar:
						machine.creaCelda(1,1,1)
						machine.preparar()
						#machine.flagPreparar = False
						print(machine.shootCounter)
			else: print("flag prep false")

			if machine.flagActiveSession and machine.flagPreparar:
				## esto va a venir de tkinter
				machine.flagPreparar = False

				while machine.flagActiveSession:
					print("aqui2")
					
					## inicio de tiros y fin de preparar 
		
					if machine.shootCounter >= 1:
						machine.nuevoTiro()
						machine.firstShooot= True
						#shootFinished == False

						#machine.shootCounter -= 1 

					if machine.firstShooot:
						machine.getData()

					if machine.flagColor == 3:

						blueCount = 1
						tirop= 5
						machine.blueAcumulate = machine.blueAcumulate + blueCount
						blueCount = 0
			
					if machine.flagColor == 2:

						redCount = 1
						tirop=-5
						machine.redAcumulate = machine.redAcumulate + redCount
						redCount = 0

					if machine.flagColor == 1:

						greenCount = 1
						tirop = 10	
						machine.greenAcumulate = machine.greenAcumulate + greenCount
						greenCount = 0

					machine.result= (machine.blueAcumulate*5) + (machine.redAcumulate * -5) + (machine.greenAcumulate * 10)

					print ("result",machine.result)
					print ("blue",machine.blueAcumulate)
					print ("red",machine.redAcumulate)
					print ("green",machine.greenAcumulate)
					lblpuntN.config(text= tirop)
					lblpuntT.config(text= machine.result)
		
					if machine.shootCounter <=0:
						machine.writeDB()
						machine.flagActiveSession= False
						salir()
			

#t1 = threading.Thread(target = lops)
#t1.daemon = True
#t1.start()
machine = Machine(100,1)

t1 = continuous_threading.PeriodicThread(0.5, mainloop)


window = Tk()

window.title("GOAL LAB")

frame_1 = Frame(height = 100, width = 480, bd = 3, relief = 'groove').place(x = 7, y = 15)
frame_2 = Frame(height = 70, width = 480, bd = 3, relief = 'groove').place(x = 7, y = 120)
frame_21= Frame(height = 70, width = 480, bd = 3, relief = 'groove').place(x = 7, y = 190)
frame_3 = Frame(height = 80, width = 480, bd = 3, relief = 'groove').place(x = 7, y = 270)
frame_4 = Frame(height = 125, width = 480, bd = 3, relief = 'groove').place(x = 7, y = 360)
#frame_4 = Frame(height = 105, width = 480, bd = 3, relief = 'groove').place(x = 7, y = 470)

    #text = Text(width = 65, height = 5)
    
    #Labels
Label(text = "Conexion").place(x = 14, y = 5)
Label(text = "Configuraciones").place(x = 14, y = 105)
Label(text = "Preparar").place(x = 14, y = 260)
Label(text = "Lanzar").place(x = 14, y = 355)
Label(text = "Baud").place(x = 122, y = 50)
Label(text = "Port").place(x = 212, y = 50)

Label(text = "Usuario", width = 13, anchor="e").place(x = 14, y = 130)
Label(text = "Id Usuario", width = 13, anchor="e").place(x = 14, y = 155)
Label(text = "Tiempo Celda (s)", width = 13, anchor="e").place(x = 14, y = 195)
Label(text = "Tiros", width = 13, anchor="e").place(x = 14, y = 215)
Label(text = "Puntaje anotacion", width = 14, anchor="e").place(x = 280, y = 380)
Label(text = "Puntaje total", width = 14, anchor="e").place(x = 280, y = 410)
lblpuntN = Label(window, width = 6, bg="#ffffff", relief=SUNKEN)
lblpuntN.place(x= 390, y=380)
lblpuntT = Label(window, width = 6, bg="#ffffff", relief=SUNKEN)
lblpuntT.place(x= 390, y=410)

lblprep = Label(window, width = 30, bg="#ffffff", relief=SUNKEN)
lblprep.place(x= 200, y=300)


#entrys

baud_entry = Entry(width = 7).place(x = 122, y = 70)    
port_entry = Entry(width = 7).place(x = 212, y = 70)
user_entry = Entry(width = 50).place(x = 130, y = 130)
id_entry = Entry(width = 50)
id_entry.place(x = 130, y = 155)
tiempoc_entry = Entry(width = 5)
tiempoc_entry.place(x = 130, y = 195)
tiros_entry = Entry(width = 5)
tiros_entry.place(x = 130, y = 215)


# butons 
button_var = IntVar()
radio_1 = Radiobutton(text = "Windows", variable = button_var, value = 1).place(x = 22, y = 30)
radio_2 = Radiobutton(text = "Linux", variable = button_var, value = 2).place(x = 122, y = 30)
b_iniciar = Button(text = "Iniciar",command = iniciar, width = 8, font = ("Verdana",9)).place(x = 14, y = 380)#, command = iniciar
b_detener = Button(text = "Detener", width = 8, font = ("Verdana",9)).place(x = 14, y = 410)#, command = detener_b

connect = Button(text = "Connect").place(x = 22, y = 70) #command = connect
disconnect = Button(text = "Disconnect").place(x =307, y = 70) #, command = disconnect
b_preparar = Button(text = "Verificar",command = prepFunction, width = 8).place(x = 40, y = 300)#, command = preparar_b


window.geometry('500x500')
t1.start()
window.mainloop()

#auxss 

#mensaje_preparar = Label(textvariable = mensaje_preparar_aux, width = 30).place(x = 200, y = 260)
#mensaje_preparar_aux.set("Realizar test primero") 
'''
mensaje_puntn_aux = StringVar() #Puntaje anotacion
mensaje_puntn = Label(textvariable = mensaje_puntn_aux, width = 6, bg="#ffffff", relief=SUNKEN)
mensaje_puntn.place(x = 320, y = 400)

mensaje_puntt_aux = StringVar() #Puntaje anotacion
mensaje_puntt = Label(textvariable = mensaje_puntn_aux, width = 6, bg="#ffffff", relief=SUNKEN)
mensaje_puntt.place(x = 320, y = 430)
'''

#mensaje_puntt_aux = StringVar() #Puntaje total, al final del ciclo
#mensaje_puntt = Label(textvariable = mensaje_puntt_aux, width = 6, bg="#ffffff", relief=SUNKEN).place(x = 390, y = 250)

'''
lbl = Label(window, text="Hello").place(x= 14, y= 6)
lbl2 = Label(window).place(x=14, y= 10)
lbl3 = Label(window).place(x=14 , y= 12)

txt = Entry(window,width=10).place(x=14 ,y=14)

btn = Button(window, text="Click Me", command=ojeto.clicked).place (x=16, y= 16)
btn2 = Button(window, text="get proces", command=ojeto.dosclick).place(x=18, y=18)

'''