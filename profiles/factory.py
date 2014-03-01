from facebook import FacebookProfile
from linkedin import LinkedinProfile
from bcfriend import BlueConnectFriend
from bcprofessional import BlueConnectProfessional
from simplecrypt import encrypt, decrypt


#key for now: change to random code generator like in 2-step auth
key = UrbcO4iQyvVk40xbY1rRKWeJ6UpPd5mg39L5FvrbBHeVGNc4Fy

"""Implemented with PyCrypto using
	AES256 algorithm"""
@staticmethod
def decrypt_profile_type(cipher):
	profile_type = decrypt(cipher, key)
	return profile_type.decode('utf8')

"""Factory * Design Pattern for creating Profiles. 
	Do NOT instanciate classes manually! Use this 
	factory method to create them."""
@staticmethod
def factory(profile_type, object):

	#delete after testing encryption
	profile_type = encrypt(key, profile_type.encode('utf8'))

	if len(profile_type) > 10:
		profile_type = decrypt_profile_type(profile_type)
	if profile_type == "Facebook": return FacebookProfile(object)
	if profile_type == "Linkedin": return LinkedinProfile(object)
	if profile_type == "BCFrd": return BlueConnectFriend(object) 
	if profile_type == "BCPro": return BlueConnectProfessional(object)
	else raise TypeError("Invalid Profile Type")