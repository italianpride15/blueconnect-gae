import abc

"""Base Class for the creation
	of Profiles types"""
class BaseProfile(profile_dict):
	__metaclass__  = abc.ABCMeta

"""Base Class for performing datastore 
	operations on Profile Classes"""
class BaseDatastore():
	__metaclass__  = abc.ABCMeta
	
	"""Profile creates a new instance of itself."""
	@abc.abstractmethod
	def post_profile(cls):
		#general implementation for super call 

	"""Profile returns itself."""
	@abc.abstractmethod
	def get_profile(cls):
		#general implementation for super call  

	"""Profile updates itself."""
	@abc.abstractmethod
	def put_profile(cls):
		#general implementation for super call 

	"""Profile deletes itself."""
	@abc.abstractmethod
	def delete_profile(cls):
		#general implementation for super call  