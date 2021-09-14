import Caesar
caesar = Caesar.Caesar()


while True:
	print("[*] Menu")
	print(":: 1) Cifrar")
	print(":: 2) Descifrar")
	print(":: 3) Salir")
	opt:int = int(input(":: "))

	if opt == 1:
		print(":[*] Escriba el mensaje a cifrar: ")
		caesar.setEncryptMsg(input("::: ").lower())
		if caesar.getEncryptMsg() != None:
			print("::[*] Mensaje Cifrado:", caesar.getEncryptMsg())
		else:
			print("::[!] Mensaje invalido.")
	elif opt == 2:
		print(":[*] Escriba el mensaje a descifrar: ")
		caesar.setUnencryptMsg(input("::: ").lower())
		if caesar.getUnencryptMsg() != None:
			print("::[*] Mensaje descifrado:", caesar.getUnencryptMsg())
		else:
			print("::[!] Mensaje invalido.")
	elif opt == 3:
		break

	print()
