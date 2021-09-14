class Vigenere:
	def __init__ (self):
		self.message = ""
		self.key = ""
		self.encoded_message = ""
		self.unencoded_message = ""

	def spanishDictionary(self):
		# Abrimos nuestro Archivo txt para leer
		file = open("dictEsp.txt", "r", encoding="utf-8")

		# Creamos una lista donde guardaremos las pa-
		# labras de nuestro txt
		# * NO QUISE USAR UN DICCIONARIO (set()) POR-
		#   QUE DESPUES PIERDE EL ORDEN ALFABETICO
		dictionary = []

		for word in file:
			# Nos aseguramos de que las palabras no
			# incluyan un salto de linea ('\n') o 
			# un espacio (' ')
			word = word.replace("\n", "")
			word = word.replace(" ", "")
			word = word
			dictionary.append(word)
		# Como el contenido del txt ya esta en nuestro
		# dictionary ya podemos cerrarlo
		file.close()

		# Como el mensaje cifrado va a contener espacios
		# agregamos uno a la lista
		dictionary.append(" ")

		numbers = "0123456789"
		for number in numbers:
			dictionary.append(number)

		return dictionary
	

	def verifyMessage(self, message):
		self.message = message.lower()
		dictionary = self.spanishDictionary()
		
		# First we have to pull apart the words of
		# the message
		list_words_message = []
		messageX = message + " "
		word = ""
		for letter in messageX:
			if letter != " ":
				word = word + letter
			else:
				list_words_message.append(word)
				word = ""
		# We delete the variable 'word'
		del word

		# Now, we can compare each word of the sentence
		# with the words of the dictionary.
		hits = 0
		for word in list_words_message:
			if word in dictionary:
				hits = hits + 1
		# Now we will calculate the percentage to know 
		# if the message corresponds to a message in spanish
		porcentage = (100 / len(list_words_message) * hits)
		if porcentage > 30:
			return True
		else:
			return False

	def verifyKey(self, message, key):
		message = message.lower()
		key = key.lower()
		key = key.replace(" ", "")
		# The key can only have letters, so:
		alphabet = "abcdefghijklmnñopqrstuvwxyz"
		for letter in key:
			if letter not in alphabet:
				key = False

		# The key minimum has to have 3 letters
		if len(key) > 2:
			# The key has to be as long as the message
			if len(key) == len(message):
				pass
			elif len(key) < len(message):
				difference = len(message) - len(key)
				actual_key = key
				key = ""
				count = 0
				for i in range(0, len(message), 1):
					if message[i] == " ":
						key = key + " "
					else:
						key = key + actual_key[count]
						count = count + 1
						if count == len(actual_key):
							count = 0
				self.key = key
			else:
				self.key = False
			return self.key
		else:
			self.key = False
			return self.key
	
	def createFlat(self):
		alphabet = "abcdefghijklmnñopqrstuvwxyz"
		flat = [[], [], [], [], [], [], [], [], [],
				[], [], [], [], [], [], [], [], [],
				[], [], [], [], [], [], [], [], []]

		# We use this meter to change of row
		count1 = 0
		# And this one to know how many places we move 
		# the alphabet
		count2 = 0
		# This 'for' is to move in the lists
		for i in range(27):
			# And this one to add the alphabet in each one
			for j in range(count2, 27, 1):
				flat[count1].append(alphabet[j])

				# We use this conditional because if we
				# moved the alphabet, the first letters
				# won't be added, so:
				if(j == 26 and count2 > 0):
					for k in range(0, count2, 1):
						flat[count1].append(alphabet[k])
			count1 = count1 + 1
			count2 = count2 + 1
		return flat

	def setEncodingMessage(self, message, key):
		message = message.lower()
		key = key.lower()
		self.encoded_message = False
		# Fiest, we have to verify if the message is really
		# encoded, so we call the 'verifyMessage' function.
		boolean = self.verifyMessage(message)
		if boolean == True:
			# Now, we have to be sure the message is as big
			# as the key, so we call the 'verify_key' function
			# and we send the message without numbers, because
			# this method doesn't cipher numbers
			short_message = message.replace("0", "")
			short_message = short_message.replace("1", " ")
			short_message = short_message.replace("2", " ")
			short_message = short_message.replace("3", " ")
			short_message = short_message.replace("4", " ")
			short_message = short_message.replace("5", " ")
			short_message = short_message.replace("6", " ")
			short_message = short_message.replace("7", " ")
			short_message = short_message.replace("8", " ")
			short_message = short_message.replace("9", " ")
			key = self.verifyKey(short_message, key)

			if key != False:
				
				
				# WE BEGIN TO ENCODE THE MESSAGE
				# FIRST, we create the flat
				flat = self.createFlat()
				
				# NOW, we can encode the message
				ciphred_message = ""
				for i in range(len(short_message)):
					coordinate1 = message[i] # short_message[i] 
					coordinate2 = key[i]


					column_pos = 0
					# Now we search the list starts with the
					# corrdinate1
					for column in flat:
						if column[0] == coordinate1:
							column = column
							break
						else:
							column_pos = column_pos + 1

					row_pos = 0
					# We do the same, but with the coordinate2
					for row in flat:
						if row[0] == coordinate2:
							row = row
							break
						else:
							row_pos = row_pos + 1
					
					if column_pos < len(row):
						ciphred_message = ciphred_message + row[column_pos]
					else:
						ciphred_message = ciphred_message + " "
				# Finally, we have to add the numbers of the origin 
				# message 
				numbers = "0123456789"
				ciphred_message = list(ciphred_message)
				for i in range(len(message)):
					if message[i] in numbers:
						ciphred_message[i] = message[i]
				self.encoded_message = "".join(ciphred_message)	

	def getEncodingMessage(self):
		return self.encoded_message

	def setUnencodingMessage(self, encoded_message, key):
		self.encoded_message = encoded_message
		encoded_message = encoded_message.replace("0", " ")
		encoded_message = encoded_message.replace("1", " ")
		encoded_message = encoded_message.replace("2", " ")
		encoded_message = encoded_message.replace("3", " ")
		encoded_message = encoded_message.replace("4", " ")
		encoded_message = encoded_message.replace("5", " ")
		encoded_message = encoded_message.replace("6", " ")
		encoded_message = encoded_message.replace("7", " ")
		encoded_message = encoded_message.replace("8", " ")
		encoded_message = encoded_message.replace("9", " ")
		key = self.verifyKey(encoded_message.lower(), key.lower())
		
		flat = self.createFlat()
		
		alphabet = "abcdefghijklmnñopqrstuvwxyz"
		# We need this encoded message copy, because we
		# don't want to use so much cycles, and we will
		# be deleting the letter alrady used
		e_message_copy = encoded_message
		unencoded_message = ""
		# Each letter we use of the kay, we will search
		# it in the begginning of each row  
		for i in key:
			for row in flat:
				# *I use this conditional to ignore the spaces
				#  because we can't encode/unencode that*
				if i == " ":
					unencoded_message = unencoded_message + " "
					e_message_copy = e_message_copy[1:]
					break
				# When find the row, we enter here
				if row[0] == i:
					count = 0
					# Now we want to find the position of each leter
					# in the row
					for letter in row:
						if letter == e_message_copy[0]:
							unencoded_message = unencoded_message + alphabet[count]
							e_message_copy = e_message_copy[1:]
							break
						count = count + 1
					break
		# We, have to be sure if the unencoded message is correct,
		# so, we call the 'verifyMessage' function
		boolean = self.verifyMessage(unencoded_message)
		
		if boolean == True:
			# Finally, we have to add the numbers of the origin 
			# message 
			numbers = "0123456789"
			unencoded_message = list(unencoded_message)
			for i in range(len(self.encoded_message)):
				if self.encoded_message[i] in numbers:
					unencoded_message[i] = self.encoded_message[i]
			self.unencoded_message = "".join(unencoded_message)
		else:
			self.unencoded_message = False

	def getUnencodingMessage(self):
		return self.unencoded_message