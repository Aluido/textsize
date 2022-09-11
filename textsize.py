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

def compararTamanno():
	if(len(text_stack) == 0):
		print("No hay cadenas de texto para comparar.\n")
		return
	else:
		print("Ingrese dos posiciones ordinales (partiendo desde 1) de cadenas a comparar.")
		pos1 = input("Posición primera cadena\n> ")
		while(not pos1.isnumeric() or int(pos1) > len(text_stack)):
			pos1 = input("Posición inválida\n> ")
		pos1 = int(pos1)

		pos2 = input("Posición segunda cadena\n> ")
		while(not pos2.isnumeric() or int(pos2) > len(text_stack)):
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