import abc
import datetime
​from google.appengine.ext import ndb

"""Base Class for the creation
	of Profiles types"""
class BaseProfile(ndb.Model, profile_dict):
	__metaclass__  = abc.ABCMeta

	key = nbd.KeyProperty(required=True)
	username = nbd.StringProperty(required=True)
	profile_type = nbd.StringProperty(required=True)
	last_modified = nbd.DateTimeProperty(required=True)
	#instant_message = db.IM()

"""Base Class for performing datastore 
	operations on Profile Classes"""
class BaseDatastore():
	__metaclass__  = abc.ABCMeta
	
	"""Profile creates a new instance of itself."""
	@abc.abstractmethod
	def post_profile(self):
		#general implementation for super call 
		last_modified = datetime.datetime.now().datetime()
		self.put()

	"""Profile returns itself."""
	@abc.abstractmethod
	def get_profile(self):
		#general implementation for super call  
		#self.toJSON()
		pass

	"""Profile updates itself."""
	@abc.abstractmethod
	def put_profile(self):
		#general implementation for super call
		last_modified = datetime.datetime.now().datetime()
		self.put() 

	"""Profile deletes itself."""
	@abc.abstractmethod
	def delete_profile(self):
		#general implementation for super call 
		self.key.delete() 