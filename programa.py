def quita_espacios(cadena):
	return [char for char in cadena if not char.isspace()]

print(quita_espacios('Hola  '))
