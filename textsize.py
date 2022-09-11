text_stack = []

# Fuente: https://stackoverflow.com/questions/196345/how-to-check-if-a-string-in-python-is-in-ascii
def isValid(string):
	try:
	    string.encode('ascii')
	except UnicodeDecodeError:
		return False
	else:
		return True

def annadirTexto():
	validText = False
	while(not validText):
		intext = input("\nEscriba el texto que desea añadir:\n> ")
		if(isValid(intext)):
			validText = True
		else:
			print("Uno o mas caracteres invalidos.")
	text_stack.append(intext.strip())
	print("Su texto ha sido añadido.\n")

def obtenerLargo():
	sizes = list(map(len, text_stack))
	return text_stack[sizes.index(max(sizes))] # retorna la primera cadena con el largo mas largo

def obtenerCorto():
	sizes = list(map(len, text_stack))
	return text_stack[sizes.index(min(sizes))] # retorna la primera cadena con el largo mas corto

	

def imprimirTexto():
	while(True):
		print("\nCadenas de texto almacenadas:", len(text_stack))
		print("Ingrese la posición ordinal (partiendo desde 1) de la cadena de texto que desee imprimir.")
		print("Funciones extra:\n[L] Imprimir cadena mas larga\t[C] Imprimir cadena mas corta")
		print("[N] Volver hacia atras.")
		intext = input("> ")
		intext = intext.casefold()

		if(intext == "n"):
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




print("Bienvenido a textsize!")
while(True):
	print("Cadenas de texto almacenadas:", len(text_stack))
	print("Seleccione una funcion:")
	print("[1] Ingresar nuevo texto")
	print("[2] Imprimir textos almacenados") # En este menú tambien se encuentra el mayor o menor tamaño
	print("[3] Comparar tamaños")
	print("[N] Salir")
	intext = input("> ")
	intext = intext.casefold()

	match intext:
		case "n":
			exit(0)
		case "1":
			annadirTexto()
		case "2":
			imprimirTexto()
		case "3":
			compararTamanno()
		case _: # default
			print("Comando Inválido.\n")