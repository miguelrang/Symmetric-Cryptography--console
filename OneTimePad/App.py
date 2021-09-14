import OneTimePad
m = OneTimePad.OneTimePad()

try:
	while True:
		print("Menu")
		print("1) Encriptar")
		print("2) Descencriptar")
		print("3) Salir")
		opt1:int = int(input(":: "))

		if opt1 == 1:
			## If you are reading this file, congratulations!!! you have discover how to decrypt with one time pad
			print("::: Escriba el texto a cifrar: ")
			msg:str = input("::: ")
			
			print(":::: ¿Desea usar una clave ya existente?")
			print(":::: 1) Si")
			print(":::: 2) No")
			opt2:int = int(input(":::: "))

			data = m.encryptedText(msg, opt2)
			print(":[*] Se a creado el archivo 'Encrypted_message.lock'")
			print(":[*] Se a creado el archivo 'Key_message.lock'")
			#print(data[0])
			#print(data[1])
			print()
		elif opt1 == 2:
			data = m.unencryptedText()
			print(":[*] Se a creado el archivo 'Unencrypted_message.lock'")
			#print(data[0])
			#print(data[1])
			#print(data[2])
			print()

		elif opt1 == 3:
				break
except:
	print("[!] Error")