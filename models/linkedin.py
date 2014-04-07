from baseclasses import BaseProfile
from baseclasses import BaseDatastore
from google.appengine.ext import ndb

class LinkedinProfile(BaseProfile, BaseDatastore):
	
	"""#let every field be indexed by default for querys
	self.email = ndb.StringProperty()
	self.full_name = ndb.StringProperty()
	self.qualities = ndb.StringProperty() #list
	self.connections = ndb.StringProperty() #list and call GQL CONTAINS #look into ReferenceProperty()
	self.address = ndb.StringProperty()
	self.curr_classes = ndb.StringProperty() #list, edu only
	self.past_classes = ndb.StringProperty() #list, linkedin/old edu
	self.major = ndb.StringProperty()
	self.minor = ndb.StringProperty()
	self.graduation = ndb.StringProperty()
	self.curr_college = ndb.StringProperty()
	self.past_colleges = ndb.StringProperty() #list
	self.highschool = ndb.StringProperty()
	self.profile_picture = ndb.BlobProperty() #default not indexed
	self.curr_job = ndb.StringProperty()
	self.past_job = ndb.StringProperty()
	self.about = ndb.TextProperty() #default not indexed
	self.approach_status = ndb.StringProperty()"""

	def __init__(self, profile_dict):
		self.key = ndb.Key(profile_dict['profile_type'], profile_dict['email'])
		self.username = profile_dict['email']
		self.profile_type = profile_dict['profile_type']
		self.email = profile_dict['email']
		self.full_name = profile_dict['full_name']
		self.qualities = profile_dict['qualities']
		self.connections = profile_dict['connections']
		self.address = profile_dict['address']
		self.curr_classes = profile_dict['curr_classes']
		self.past_classes = profile_dict['past_classes']
		self.major = profile_dict['major']
		self.minor = profile_dict['minor']
		self.graduation = profile_dict['graduation']
		self.curr_college = profile_dict['curr_college']
		self.past_colleges = profile_dict['past_colleges']
		self.highschool = profile_dict['highschool']
		self.profile_picture = profile_dict['profile_picture']
		self.curr_job = profile_dict['curr_job']
		self.past_job = profile_dict['past_job']
		self.about = profile_dict['about']
		self.approach_status = profile_dict['approach_status']

	"""Following functions are implemented from 
		BaseDatastore with super() implementation.
		See baseclass for general implementation."""

	"""Insert concrete implementation documentation"""
	@classmethod
	def post_profile(self):
		super(LinkedinProfile, self).post_profile()
	
	"""Insert concrete implementation documentation"""
	@classmethod
	def get_profile(self):
		super(LinkedinProfile, self).get_profile()

	"""Insert concrete implementation documentation"""
	@classmethod
	def put_profile(self):
		super(LinkedinProfile, self).put_profile()

	"""Insert concrete implementation documentation"""
	@classmethod
	def delete_profile(self):
		super(LinkedinProfile, self).delete_profile()