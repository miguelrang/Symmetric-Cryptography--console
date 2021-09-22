import Enigma
e = Enigma.Enigma()


print("[*] Escriba su mensaje (no debe contener espacios):")
msg:str = input().upper()
msg = msg.replace("ñ", "")

print("[*] Escriba la clave (deben ser 3 letras):")
key:str = input().upper()
key = key.replace("ñ", "")

print("[*] Escriba el orden de los rotores (ejemplo: 2 1 3)")
rotores:str = input()

final_msg:str = e.enigma(msg, key, rotores)
if final_msg == "":
	print("[!] Ah ocurrido un error, verifique que los datos\n::: añadidos sean validos")
else:
	print("[*] El mensaje es:", final_msg)
