from simplecrypt import encrypt, decrypt

class Authentication():

	"""Implemented with PyCrypto using
		AES256 algorithm"""
	@staticmethod
	def decrypt_profile_type(cipher):
		#key for now: change to random code generator like in 2-step auth
		key = 'UrbcO4iQyvVk40xbY1rRKWeJ6UpPd5mg39L5FvrbBHeVGNc4Fy'
		profile_type = decrypt(key, cipher)
		return profile_type.decode('utf8')