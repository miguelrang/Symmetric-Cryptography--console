import Ascitala
ascitala = Ascitala.Ascitala()


while True:
	print("[*] Menú")
	print(":: 1) Cifrar")
	print(":: 2) Descifrar")
	print(":: 3) Salir")
	opt:int = int(input(":: "))

	if opt == 1:
		print(":[*] Escriba el mensaje a cifrar: ")
		ascitala.setMsg(msg=input(":::: "))
		if ascitala.getMsg() == None:
			print(":[!] Mensaje Invalido")
			break

		print(":[*] Escriba la clave de su mensaje(column row): ")
		ascitala.setKey(key=input(":::: "))
		if ascitala.getKey() == None:
			print(":[!] Clave Invalida")
			break

		encrypted_msg = ascitala.encryptingMsg(ascitala.getMsg(), 
			ascitala.getKey())
		print("Mensaje:\t", ascitala.getMsg())
		print("Clave:\t\t " + str(ascitala.getKey()[0]) + "x" + str(ascitala.getKey()[1]))
		print("Cifrado:\t", encrypted_msg)

	elif opt == 2:
		print(":[*] Escriba el mensaje cifrado: ")
		ascitala.setEncryptedMsg(encrypted_msg=input())
		if ascitala.getEncryptedMsg() == None:
			print(":[!] Mensaje Cifrado Invalido")
			break

		print(":[*] Escriba la clave para decifrar(column row): ")
		ascitala.setKey(key=input())
		if ascitala.getKey() == None:
			print(":[!] Clave Invalida")
			break

		unencrypted_msg = ascitala.unencryptingMsg(ascitala.getEncryptedMsg(), 
			ascitala.getKey())
		print("Mensaje Cifrado:", ascitala.getEncryptedMsg())
		print("Clave:\t\t\t " + str(ascitala.getKey()[0]) + "x" + str(ascitala.getKey()[1]))
		print("Descifrado:\t\t", unencrypted_msg)

	elif opt == 3:
		break