import random


class OneTimePad:
	def __init__(self):
		pass
		

	def becomeTextToBytesList(self, text:str):
 		# M E S S A G E
		byte_text = bytes(text, "ascii")
		bytes_list:list = []
		for byte in byte_text:
			bytes_list.append(byte)
		return bytes_list

	def becomeBytesToCharsList(self, bytes_unencrypted:bytes):
		chars_list:list = []
		for byte in bytes_unencrypted:
			chars_list.append(byte.to_bytes(1, "big"))

		return chars_list

	def randomKey(self, message:str):
		# K E Y
		bytes_list:list = []
		for i in range(len(message)):
			bytes_list.append(random.randint(0, 255))
		return bytes_list

	def encryptedText(self, text:str, opt:int):
		# In this variable we save the 
		# unencoded message but in bytes 
		# (for this we call the becomeTextToBytesList
		#  function)
		bytes_msg:list = self.becomeTextToBytesList(text)
		
		# If you chose to use an old key, we enter
		# to the first option
		bytes_key:list = []
		if opt == 1:
			with open("Key_message.lock", "rb") as file:
				data = file.read()
			for i in data:
				bytes_key.append(i)
		
		elif opt == 2:
			# If you want a new key, we create it for you
			bytes_key = bytearray(self.randomKey(bytes_msg))
			with open("Key_message.lock", "wb") as file:
				file.write(bytes_key)


		bytes_encrypted:list = []
		i:int = 0
		while i < len(bytes_key):
			bytes_encrypted.append((bytes_msg[i] ^ bytes_key[i]))
			i+=1
		bytes_encrypted = bytearray(bytes_encrypted)
		with open("Encrypted_message.lock", "wb") as file:
			file.write(bytes_encrypted)
		return bytes_encrypted, bytes_key
		

	def unencryptedText(self):
		with open("Encrypted_message.lock", "rb") as file:
			data_e_m = file.read()
		bytes_enc_msg:list = []
		for i in data_e_m:
			bytes_enc_msg.append(i)

		with open("Key_message.lock", "rb") as file:
			data_k_m = file.read()
		bytes_key_msg:list = []
		for i in data_k_m:
			bytes_key_msg.append(i)

		i:int = 0
		bytes_unencrypted = []
		while i < len(bytes_key_msg):
			bytes_unencrypted.append(bytes_enc_msg[i] ^ bytes_key_msg[i])
			i+=1
		
		bytes_unencrypted_array = bytearray(bytes_unencrypted)
		with open("Unencrypted_message.lock", "wb") as file:
			file.write(bytes_unencrypted_array)
		text_unencrypted = b"".join(self.becomeBytesToCharsList(bytes_unencrypted))
		
		return text_unencrypted, bytes_unencrypted, bytes_key_msg
