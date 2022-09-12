import logging


logging.basicConfig(filename='textsize.log', encoding='utf-8', level=logging.DEBUG)
text_stack = []

# Fuente: https://stackoverflow.com/questions/196345/how-to-check-if-a-string-in-python-is-in-ascii
def isValid(string):
	try:
	    string.encode('ascii')
	except UnicodeDecodeError:
		logging.warning("La cadena ingresada posee caracteres invalidos no ASCII.")
		return False
	else:
		logging.info("La cadena ingresada (%s) es válida.", string)
		return True

def annadirTexto():
	validText = False
	while(not validText):
		intext = input("\nEscriba el texto que desea añadir:\n> ")
		logging.info("Texto ingresado por el usuario: %s", intext)
		if(isValid(intext)):
			validText = True
		else:
			print("Uno o mas caracteres invalidos.")
	intext = intext.strip()
	text_stack.append(intext)
	logging.info("Texto guardado en la pila: %s", intext)
	print("Su texto ha sido añadido.\n")

def obtenerLargo():
	sizes = list(map(len, text_stack))
	logging.info("Activacion funcion de encontrar cadena mas larga.")
	return text_stack[sizes.index(max(sizes))] # retorna la primera cadena con el largo mas largo

def obtenerCorto():
	sizes = list(map(len, text_stack))
	logging.info("Activacion funcion de encontrar cadena mas corta.")
	return text_stack[sizes.index(min(sizes))] # retorna la primera cadena con el largo mas corto

	

def imprimirTexto():
	while(True):
		print("\nCadenas de texto almacenadas:", len(text_stack))
		print("Ingrese la posición ordinal (partiendo desde 1) de la cadena de texto que desee imprimir.")
		print("Funciones extra:\n[L] Imprimir cadena mas larga\t[C] Imprimir cadena mas corta")
		print("[N] Volver hacia atras.")
		intext = input("> ")
		logging.info("Texto ingresado por el usuario: %s", intext)
		intext = intext.casefold()

		if(intext == "n"):
			logging.info("Usuario sale del menú de impresión de textos.")
			return
		elif (intext == "l"): # largo
			print(obtenerLargo())
		elif (intext == "c"): # corto
			print(obtenerCorto())
		elif (intext.isnumeric()): # posicion
			if(int(intext) > len(text_stack)):
				print("\nPosicion inalcanzable.")
			else:
				print("\nTu cadena:", text_stack[int(intext)-1])
		else:
			print("\nComando Inválido.")

def compararTamanno():
	if(len(text_stack) == 0):
		logging.warning("Acceso a comparacion de cadenas sin cadenas que comparar.")
		print("No hay cadenas de texto para comparar.\n")
		return
	else:
		print("Ingrese dos posiciones ordinales (partiendo desde 1) de cadenas a comparar.")
		pos1 = input("Posición primera cadena\n> ")
		logging.info("Texto ingresado por el usuario: %s", intext)
		while(not pos1.isnumeric() or int(pos1) > len(text_stack)):
			logging.warning("Se ingresó una posición inválida.")
			pos1 = input("Posición inválida\n> ")
		pos1 = int(pos1)

		pos2 = input("Posición segunda cadena\n> ")
		logging.info("Texto ingresado por el usuario: %s", intext)
		while(not pos2.isnumeric() or int(pos2) > len(text_stack)):
			logging.warning("Se ingresó una posición inválida.")
			pos2 = input("Posición inválida\n> ")
		pos2 = int(pos2)

		print("\nComparativa:")
		print("Tamaño cadena 1:", len(text_stack[pos1-1]))
		print("Tamaño cadena 2:", len(text_stack[pos2-1]))
		if(len(text_stack[pos1-1]) > len(text_stack[pos2-1])):
			print("La cadena 1 (" + text_stack[pos1-1]+ ") es mas larga que la cadena 2 (" + text_stack[pos2-1] + ").\n")
		else:
			print("La cadena 2 (" + text_stack[pos2-1]+ ") es mas larga que la cadena 1 (" + text_stack[pos1-1] + ").\n")



print("Bienvenido a textsize!")
while(True):
	print("Cadenas de texto almacenadas:", len(text_stack))
	print("Seleccione una funcion:")
	print("[1] Ingresar nuevo texto")
	print("[2] Imprimir textos almacenados") # En este menú tambien se encuentra el mayor o menor tamaño
	print("[3] Comparar tamaños")
	print("[N] Salir")
	intext = input("> ")
	logging.info("Texto ingresado por el usuario: %s", intext)
	intext = intext.casefold()

	match intext:
		case "n":
			logging.info("Programa terminado satisfactoriamente por el usuario.")
			exit(0)
		case "1":
			logging.info("Acceso al menu 1, añadir texto.")
			annadirTexto()
		case "2":
			logging.info("Acceso al menu 2, impresión de texto.")
			imprimirTexto()
		case "3":
			logging.info("Acceso al menu 3, comparacion de tamaños.")
			compararTamanno()
		case _: # default
			logging.warning("Comando inválido en el menú.")
			print("Comando Inválido.\n")