import re


class Ascitala:
	def __init__(self):
		self.msg:str = ""
		self.key:list = []
		self.encrypted_msg:str = ""

	def setMsg(self, msg:str):
		chars = "|¬°!\"#$%&/()='?\\¿¡´¨+*~{[^}]`,;.:-_<> "
		# If any character is in the message, we delate that
		for char in msg:
			if char in chars:
				msg = msg.replace(f"{char}", "")
		if len(msg) > 0:
			self.msg:str = msg
		else:
			self.msg = None

	def getMsg(self):
		return self.msg

	def setEncryptedMsg(self, encrypted_msg:str):
		chars = "|¬°!\"#$%&/()='?\\¿¡´¨+*~{[^}]`,;.:-_<> "
		for char in encrypted_msg:
			if(char not in chars and 
				len(encrypted_msg) > 0):
				self.encrypted_msg:str = encrypted_msg
			else:
				self.encrypted_msg = None

	def getEncryptedMsg(self):
		return self.encrypted_msg

	def setKey(self, key:str):
		expr = re.compile(r"\d \d")
		valid = expr.fullmatch(key)
		if valid:
			self.key.append(int(key[0]))
			self.key.append(int(key[2]))
		else:
			self.key = None

	def getKey(self):
		return self.key

	def encryptingMsg(self, msg:str, key:list):
		# First, we have to create our matrix
		matrix:list = [" "*key[1]]*key[0]
		# and then, we become the list of strings
		# to a list of lists
		for i in range(len(matrix)):
			matrix[i] = list(matrix[i])
		# We write the message in the matrix
		count:int = 0
		for i in range(key[1]):
			for place in matrix:
				place[i] = msg[count]
				count = count + 1
		# We become our matrix to text
		for i in range(len(matrix)):
			matrix[i]:str = "".join(matrix[i])
		# Finally, we return the encoded message
		return "".join(matrix)

	def unencryptingMsg(self, encrypted_msg:str, key:list):
		# First we generate the matrix with the key
		# but in now we invert the dimensions
		matrix:list = [" "*key[0]]*key[1]
		# and then, we become the list of strings
		# to a list of lists
		for i in range(len(matrix)):
			matrix[i] = list(matrix[i])
		# We write the encoded message in the matrix
		count:int = 0
		for i in range(key[0]):
			for place in matrix:
				place[i] = encrypted_msg[count]
				count = count + 1
		# We become our matrix to text
		for i in range(len(matrix)):
			matrix[i]:str = "".join(matrix[i])
		# Finally, we return the unencoded message
		return "".join(matrix)

