text_stack = []

def añadirTexto():
	validText = False
	while(not validText):
		intext = input("\nEscriba el texto que desea añadir:\n> ")
		if(isValid(intext)):
			validText = True
		else:
			print("Uno o mas caracteres invalidos.")
	text_stack.append(intext.strip())
	print("Su texto ha sido añadido.\n")
	return

# Fuente: https://stackoverflow.com/questions/196345/how-to-check-if-a-string-in-python-is-in-ascii
def isValid(string):
	try:
	    string.encode('ascii')
	except UnicodeDecodeError:
		return False
	else:
		return True

print("Bienvenido a textsize!")
while(True):
	print("Cadenas de texto almacenadas:", len(text_stack))
	print("Seleccione una funcion:")
	print("[1] Ingresar nuevo texto")
	print("[2] Imprimir textos almacenados") # En este menú tambien se encuentra el mayor o menor tamaño
	print("[3] Comparar tamaños")
	print("[N] Salir")
	intext = input("> ")

	match intext.casefold():
		case "n":
			exit(0)
		case "1":
			añadirTexto()
		case _: # default
			print("Comando Inválido.\n")