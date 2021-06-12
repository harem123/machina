from tkinter import *
import time
import threading
import continuous_threading

class objectR(object):

	def __init__(self):

		self.res = 0
		self.dataIn = 0
		self.flag = False
		self.delTh = 0
		self.ts = 0

	def clicked(self):

	    self.res = txt.get()

	    self.dataIn = int(self.res)
	    
	    lbl2.configure(text= self.res)

	def dosclick(self):

		dataProc = self.dataIn + 20

		lbl3.configure(text= dataProc)

	

	    
ojeto = objectR()
#mensaje_puntn_aux.set("")
def printer():

	for x in range(0, 22):
		print("We're on %d time" % (x))
		if x== 15:
			ojeto.delTh = 100
		if x== 20:
			ojeto.delTh = 200
		time.sleep(0.2)
		if ojeto.flag:
			lblpuntN.config(text= ojeto.delTh)
			ojeto.ts = int(tiempoc_entry.get())
			result= ojeto.ts + 100
			print(result)

			
t1 = continuous_threading.PeriodicThread(0.5, printer)

def iniciando():
	ojeto.flag =True

def geters():
	ojeto.ts = int(tiempoc_entry.get())



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

lblpuntT = Label(window, width = 30, bg="#ffffff", relief=SUNKEN)
lblpuntT.place(x= 200, y=300)

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
b_iniciar = Button(text = "Iniciar",command = geters, width = 8, font = ("Verdana",9)).place(x = 14, y = 380)#, command = iniciar
b_detener = Button(text = "Detener", width = 8, font = ("Verdana",9)).place(x = 14, y = 410)#, command = detener_b

connect = Button(text = "Connect").place(x = 22, y = 70) #command = connect
disconnect = Button(text = "Disconnect").place(x =307, y = 70) #, command = disconnect
b_preparar = Button(text = "Verificar",command = iniciando, width = 8).place(x = 40, y = 300)#, command = preparar_b

'''
lbl = Label(window, text="Hello").place(x= 14, y= 6)
lbl2 = Label(window).place(x=14, y= 10)
lbl3 = Label(window).place(x=14 , y= 12)

txt = Entry(window,width=10).place(x=14 ,y=14)

btn = Button(window, text="Click Me", command=ojeto.clicked).place (x=16, y= 16)
btn2 = Button(window, text="get proces", command=ojeto.dosclick).place(x=18, y=18)

'''
window.geometry('500x500')
t1.start()
window.mainloop()


