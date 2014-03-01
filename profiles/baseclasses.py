#http://python-3-patterns-idioms-test.readthedocs.org/en/latest/Factory.html#preventing-direct-creation
import abc

"""Base Class for the creation
	of Profiles types"""
class BaseProfile(object):
	__metaclass__  = abc.ABCMeta

"""Base Class for performing datastore 
	operations on Profile Classes"""
class BaseDatastore():
	__metaclass__  = abc.ABCMeta

	#maybe __init__ with cls so can call self. for each function
	
	#general implementation so can call super 
	@abc.abstractmethod
	def post_profile(cls):
		"""Profile creates a new instance of itself."""
	
	@abc.abstractmethod
	def get_profile(cls):
		"""Profile returns itself."""

	@abc.abstractmethod
	def put_profile(cls):
		"""Profile updates itself."""

	@abc.abstractmethod
	def delete_profile(cls):
		"""Profile deletes itself."""
