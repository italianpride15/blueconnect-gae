from facebook import FacebookProfile
from linkedin import LinkedinProfile
from bcfriend import BlueConnectFriend
from bcprofessional import BlueConnectProfessional
#from helpers.authentication import Authentication

class ProfileFactory():

	"""Abstract Factory Design Pattern for creating Profiles. Do NOT 
		instanciate classes manually! Use the register method to create them."""
	@staticmethod
	def register(profile_type, profile_dict):
		
		#profile_type = Authentication.decrypt_profile_type(profile_cipher)

		"""This code block will update info from external service (Facebook,
			Linkedin, etc) using token or refresh token"""
		if profile_type == "Facebook" and type(profile_dict) is str: 
			#WILL NEED TO GET TOKEN SOMEHOW/use refresh token
			#make facebook api call and put data in dict
			FacebookProfile(profile_dict).put()
			#return status_code
		if profile_type == "Linkedin" and type(profile_dict) is str: 
			#WILL NEED TO GET TOKEN SOMEHOW/use refresh token
			#make linkedin api call and put data in dict
			LinkedinProfile(profile_dict).put()
			#return status_code
		"""This code block will update info from the dictionary sent up
			by user. Fields that they changed should now remain static"""
		if profile_type == "Facebook" and type(profile_dict) is dict: 
			#figure out how to not allow fields the user changed to be modifed from external service
			FacebookProfile(profile_dict).put()
			#return status_code
		if profile_type == "Linkedin" and type(profile_dict) is dict:
			#figure out how to not allow fields the user changed to be modifed from external service
			LinkedinProfile(profile_dict).put()
			#return status_code
		"""This code block will always update with user's curr app info
			since they do not use any external services"""
		if profile_type == "BCFrd": 
			BlueConnectFriend(profile_dict).put() 
			#return status_code
		if profile_type == "BCPro": 
			BlueConnectProfessional(profile_dict).put()
			#return status_code
		else: raise TypeError("Invalid Profile Type")