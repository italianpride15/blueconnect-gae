from models.factory import ProfileFactory
from google.appengine.ext import ndb
#from simplecrypt import encrypt, decrypt

class EndpointsInterfaceToDatastore():

	"""This class provides an interface from the endpoints to the profiles
		in the datastore. After the profile is retrieved from the database, 
		its respective method is called on itself."""
		
	@staticmethod
	def get_profile(profile_type, username): #pass profile_cipher?
		#profile_type = Authentication.decrypt_profile_type(profile_cipher)
		user_key = ndb.Key(profile_type, username)
		user = user_key.get()
		return user.get_profile()

	@staticmethod
	def post_profile(profile_type, profile_dict):
		response = ProfileFactory.register(profile_type, profile_dict)	
		return response	

	@staticmethod
	def put_profile(profile_type, profile_dict):
		response = ProfileFactory.register(profile_type, profile_dict)
		return response		

	@staticmethod
	def delete_profile(profile_type, username):
		#profile_type = Authentication.decrypt_profile_type(profile_cipher)
		user_key = ndb.Key(profile_type, username)
		user = user_key.get()
		response = user.delete_profile()
		return response
