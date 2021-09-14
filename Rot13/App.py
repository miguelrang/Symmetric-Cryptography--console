import Rot13
rot13 = Rot13.Rot13()


while True:
	print("[*] Menu")
	print(":: 1) Cifrar")
	print(":: 2) Descifrar")
	print(":: 3) Salir")
	opt:int = int(input(":: "))

	if opt == 1:
		print(":[*] Escriba el mensaje a cifrar: ")
		rot13.setEncryptMsg(input("::: ").lower())
		if rot13.getEncryptMsg() != None:
			print("::[*] Mensaje Cifrado:", rot13.getEncryptMsg())
		else:
			print("::[!] Mensaje invalido.")
	elif opt == 2:
		print(":[*] Escriba el mensaje a descifrar: ")
		rot13.setUnencryptMsg(input("::: ").lower())
		if rot13.getUnencryptMsg() != None:
			print("::[*] Mensaje descifrado:", rot13.getUnencryptMsg())
		else:
			print("::[!] Mensaje invalido.")
	elif opt == 3:
		break

	print()
