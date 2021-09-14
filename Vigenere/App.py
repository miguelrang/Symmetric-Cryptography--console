from Vigenere import Vigenere as v
v = v()


while True:
	print("[*] Menu")
	print("::: 1) Cifrar mensaje")
	print("::: 2) Descifrar mensaje")
	print("::: 3) Salir")
	opt = int(input(":::: "))

	if opt == 1 or opt == 2:
		if opt == 1:
			v.setEncodingMessage(input(":[*] Escriba el mensaje a cifrar:\n:::: "),
									input(":[*] Escriba la clave para su mensaje:\n:::: "))
			

			if v.getEncodingMessage() == False:
				print()
				print(":[!] El mensaje que agregó ya esta cifrado")
				print(":::: o esta mal escrito.")
			else:
				print("::[*] Texto Plano:\t\t", v.message)
				print("::[*] Clave:\t\t\t", v.key.replace(" ", ""))
				print("::[*] Mensaje Cifrado:\t", v.getEncodingMessage())
			print()
		
		elif opt == 2:
			v.setUnencodingMessage(input(":[*] Escriba el mensaje a descifrar:\n:::: "),
									input(":[*] Escriba la clave de su mensaje:\n:::: "))


			if v.getUnencodingMessage() == False:
				print()
				print(":[!] El mensaje cifrado o clave que agrego\n:::: son incorrectos.")
			else:
				print("::[*] Mensaje Cifrado:\t\t", v.encoded_message)
				print("::[*] Clave:\t\t\t", v.key.replace(" ", ""))
				print("::[*] Mensaje Descifrado:\t", v.getUnencodingMessage())
			print()
	elif opt == 3:
		print("[*] Cerrando programa...")
		break
		