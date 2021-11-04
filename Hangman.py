import random
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from PIL import ImageTk, Image
import sys




def ImportarPalabras():
	archivo=open("Palabras.txt","r")
	tempList=archivo.readlines()
	archivo.close()
	wordList=[]
	for linea in tempList:
		linea=linea.strip()
		wordList.append(linea)
	del(tempList)
	return wordList
def ElegirPalabra():
	global listaDePalabras
	return listaDePalabras[random.randint(0,len(listaDePalabras)-1)]
def Chequear(caracter):
	global palabra
	global intentos
	global palabraOfuscada
	global caracterIngresado
	global listaLetrasIngresadas
	global listaLetrasIngresadasTotales
	global gameOn

	caracter = caracter.lower()
	#auxIngresadas=listaLetrasIngresadas.get()
	auxIngresadas=listaLetrasIngresadas.get()

	if gameOn:

		if caracter in listaLetrasIngresadasTotales:
			messagebox.showinfo("Error","La letra ya ha sido ingresada anteriormente")
			caracterIngresado.set("")
		else:
			if len(caracter) > 1 or len(caracter) == 0 or caracter.isdigit():
				messagebox.showinfo("Error","Solo se puede ingresar solo una letra/caracter.")
				caracterIngresado.set("")
			else:
				auxIngresadas = auxIngresadas + caracter + " - "
				listaLetrasIngresadasTotales = listaLetrasIngresadasTotales + caracter
				#listaLetrasIngresadas.set(auxIngresadas)
				aux=palabraOfuscada.get()
				newOfus=""
				listaAux=[]

				for i in range(len(aux)):
					listaAux.append(aux[i])

				if caracter in palabra:
					for i in range(len(palabra)):
						if palabra[i] == caracter:
							listaAux[i*2] = caracter
				else:
					listaLetrasIngresadas.set(auxIngresadas)
					intentos = intentos + 1
					CambiarImagen(intentos)


				nuevaString=""
				for i in range(len(listaAux)):
					nuevaString = nuevaString + listaAux[i]

				palabraOfuscada.set(nuevaString)
				caracterIngresado.set("")

				if "_" not in nuevaString:
					messagebox.showinfo("Felicitaciones","Has ganado.")
					gameOn=False
def CambiarImagen(intentos):
	global imagenes
	global imagenAhorcado
	global i1
	global gameOn
	global palabra

	auxImage=imagenes[intentos].resize((150,150), Image.ANTIALIAS)
	i1 = ImageTk.PhotoImage(auxImage)
	imagenAhorcado.config(image=i1)
	if intentos == 7:
		gameOn=False
		messagebox.showinfo("Tristeza","Ya no te quedan intentos. La palabra a buscar era "+palabra +".")
def NuevoJuego():
	global palabra
	global longitud
	global intentos
	global gameOn
	global imagenes
	global imagenAhorcado
	global caracterIngresado
	global listaLetrasIngresadas
	global palabraOfuscada
	global listaLetrasIngresadasTotales

	palabra=ElegirPalabra()
	longitud=len(palabra)
	intentos=0
	gameOn=True
	CambiarImagen(0)

	caracterIngresado.set("")
	listaLetrasIngresadas.set("      ")
	auxString=""
	for i in range(longitud):
		auxString = auxString + "_ "
	palabraOfuscada.set(auxString)

	listaLetrasIngresadasTotales=""
def About():
	messagebox.showinfo("Informacion del Autor",
		"Nombre: E. Gastón Rayes\nGithub: github.com/voltum3l/")
def Exit():
	option=messagebox.askquestion("Salir","¿Cerrar el programa?")
	if option=="yes":
		sys.exit()

gameOn=True
listaDePalabras=ImportarPalabras()
palabra=ElegirPalabra()
listaLetrasIngresadasTotales=""
longitud=len(palabra)
intentos=0

### -------- TKINTER ----------- ###

root = Tk()
root.title("HangMan")
root.config(bg="white")

######   MENU

barraMenu=Menu(root)
root.config(menu=barraMenu)
fileMenu=Menu(barraMenu,tearoff=0)

fileMenu.add_command(label="Nuevo Juego",command=NuevoJuego)
fileMenu.add_separator()
fileMenu.add_command(label="Exit")

acercaDe=Menu(barraMenu,tearoff=0)
acercaDe.add_command(label="Desarrollador",command=About)

barraMenu.add_cascade(label="File",menu=fileMenu)
barraMenu.add_cascade(label="Info",menu=acercaDe)

######


frame0=Frame(root,bg="white")
frame0.config(width="400",height="50")
frame0.grid(row=0,column=0,sticky="n",pady=5)

#imagenes=[Image.open('\\images\\0.png'),Image.open('\\images\\1.png'),Image.open('\\images\\2.png'),Image.open('\\images\\3.png'),Image.open('\\images\\4.png'),Image.open('\\images\\5.png'),Image.open('\\images\\6.png'),Image.open('\\images\\7.png')]
imagenes=[Image.open('0.png'),Image.open('1.png'),Image.open('2.png'),Image.open('3.png'),Image.open('4.png'),Image.open('5.png'),Image.open('6.png'),Image.open('7.png')]
image1=imagenes[0].resize((150,150), Image.ANTIALIAS)
i1 = ImageTk.PhotoImage(image1)
imagenAhorcado=Label(frame0,image=i1)
imagenAhorcado.grid(row=0,column=0,pady=1,padx=1,sticky="nsew")

listaLetrasIngresadas=StringVar()

listaLetrasIngresadas.set("     ")

CartelletrasIngresadas=Label(frame0,text="Letras Ingresadas",fg="black",font=('bold',9))
CartelletrasIngresadas.grid(row=1,column=0,pady=2,sticky="nsew")
letrasIngresadas=Label(frame0,textvariable=listaLetrasIngresadas,fg="black",font=('bold',8))
letrasIngresadas.grid(row=2,column=0,sticky="nsew")

frame1=Frame(root,bg="white")
frame1.config(width="400",height="50")
frame1.grid(row=1,column=0,sticky="n",pady=3)

palabraOfuscada=StringVar()
auxString=""

for i in range(longitud):
	auxString = auxString + "_ "

palabraOfuscada.set(auxString)
ofus=Label(frame1,textvariable=palabraOfuscada,fg="red",font=('bold',19))
ofus.grid(row=0,column=0,pady=30)
emptyLabel=Label(frame1,text=" ",fg="white",font=(25))
ofus.grid(row=1,column=0)


caracterIngresado=StringVar()

frame2=Frame(root,bg="white")
frame2.config(width="400",height="50")
frame2.grid(row=2,column=0,sticky="n",pady=3)
ingresarLabel=Label(frame2,text=">>>>> ",fg="black",font=('bold',14))
ingresarLabel.grid(row=0,column=0,pady=2)
entryInput=Entry(frame2,bg="black",fg="white",textvariable=caracterIngresado,font=('bold',14))
entryInput.grid(row=0,column=1,padx=2)
entryInput.config(justify="center")
entryButton=Button(frame2,text="Ingresar",width=7,height=1)
entryButton.grid(row=0,column=2,padx=1)
entryButton.config(command=lambda:Chequear(caracterIngresado.get()))

root.mainloop()

"""
while intentos < 6:
	caracter=input("Ingrese caracter>> ")
	if caracter in palabra:
		vecesQueAparece=palabra.count(caracter)
		for i in range(len(palabra)):
			if palabra[i] == caracter:
				pass
	else:
		print("No está")	
		intentos += 1
"""


