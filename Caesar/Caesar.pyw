class Caesar:
	def __init__(self):
		self.encrypted_msg:str = ""
		self.unencrypted_msg:str = ""

	def dictSpanish(self):
		dict_spanish:list = []
		with open("dictEsp.txt", "r", encoding="UTF-8") as file:
			dict_spanish = file.readlines()
		
		dif_as:list = list("áäà")
		dif_es:list = list("éëè")
		dif_is:list = list("íïì")
		dif_os:list = list("óöò")
		dif_us:list = list("úüù")

		for i in range(len(dict_spanish)):
			dict_spanish[i] = dict_spanish[i].replace("\n", "")
			
			for letter in dict_spanish[i]:
				if letter in dif_as:
					dict_spanish[i] = dict_spanish[i].replace(letter, "a")
				if letter in dif_es:
					dict_spanish[i] = dict_spanish[i].replace(letter, "e")
				if letter in dif_is:
					dict_spanish[i] = dict_spanish[i].replace(letter, "i")
				if letter in dif_os:
					dict_spanish[i] = dict_spanish[i].replace(letter, "o")
				if letter in dif_us:
					dict_spanish[i] = dict_spanish[i].replace(letter, "u")

		return dict_spanish

	def becomeMsgToList(self, msg:str):
		words_msg:list = []
		word:str = ""
		count:int = 0
		dif_as:list = list("áäà")
		dif_es:list = list("éëè")
		dif_is:list = list("íïì")
		dif_os:list = list("óöò")
		dif_us:list = list("úüù")
		for char in msg:
			if char in dif_as:
				msg = msg.replace(char, "a")
			if char in dif_es:
				msg = msg.replace(char, "e")
			if char in dif_is:
				msg = msg.replace(char, "i")
			if char in dif_os:
				msg = msg.replace(char, "o")
			if char in dif_us:
				msg = msg.replace(char, "u")

			if char == " ":
				words_msg.append(word)
				word = ""
			else:
				word = word + char
				if count == len(msg)-1:
					words_msg.append(word)

			count = count + 1
		return words_msg

	def verifyMsg(self, msg:str):
		# We become the message to list, to compire
		# the words easier with the words list of the 
		# dictionary
		words_msg:list = self.becomeMsgToList(msg)
		# we save the dictionary in this list
		dict_spanish:list = self.dictSpanish()
		# we use this variable to know if the message
		# looks like a spanish message
		count:int = 0 
		for word in words_msg:
			if word in dict_spanish:
				count = count + 1
		# Now, we use a simple rule of 3 10/100
		try:
			porcentage:float = (len(words_msg)*100)/count
			if porcentage > 30:
				return msg
			else:
				return None
		except:
			return None
			

	def setEncryptMsg(self, msg:str):
		msg:str = self.verifyMsg(msg)
		key = 3

		if msg != None:
			alphabet:str = "abcdefghijklmnñopqrstuvwxyz"
			encrypted_msg:str = ""
			for letter in msg:
				for i in range(len(alphabet)-1):
					if alphabet[i] == letter or letter == " ":
						if letter == " ":
							encrypted_msg = encrypted_msg + " "
						else:
							if i+key > len(alphabet)-1:
								pos:int = i+key - len(alphabet)-1
								encrypted_msg = encrypted_msg + alphabet[pos]
								del pos
							else:
								encrypted_msg = encrypted_msg + alphabet[i+key]
						break
			self.encrypted_msg = encrypted_msg
		else:
			self.encrypted_msg = None

	def getEncryptMsg(self):
		return self.encrypted_msg

	def setUnencryptMsg(self, encrypted_msg):
		# In this function it's the same, but inverted
		encrypted_msg:str = encrypted_msg
		key = 3

		alphabet:str = "abcdefghijklmnñopqrstuvwxyz"
		unencrypted_msg:str = ""
		for letter in encrypted_msg:
			for i in range(len(alphabet)-1):
				if alphabet[i] == letter or letter == " ":
					if letter == " ":
						unencrypted_msg = unencrypted_msg + " "
					else:
						if i-key < 0:
							pos:int = i-key + len(alphabet)-1
							unencrypted_msg = unencrypted_msg + alphabet[pos]
							del pos
						else:
							unencrypted_msg = unencrypted_msg + alphabet[i-key]
					break

		unencrypted_msg = self.verifyMsg(unencrypted_msg)
		self.unencrypted_msg = unencrypted_msg
	
		
	def getUnencryptMsg(self):
		return self.unencrypted_msg	


