from baseclasses import BaseProfile
from baseclasses import BaseDatastore

class LinkedinProfile(BaseProfile, BaseDatastore):
	
	#let every field be indexed by default for querys
	self.email = nbd.StringProperty()
	self.full_name = nbd.StringProperty()
	self.qualities = nbd.StringProperty() #list
	self.connections = nbd.StringProperty() #list and call GQL CONTAINS #look into ReferenceProperty()
	self.address = nbd.StringProperty()
	self.curr_classes = nbd.StringProperty() #list, edu only
	self.past_classes = nbd.StringProperty() #list, linkedin/old edu
	self.major = nbd.StringProperty()
	self.minor = nbd.StringProperty()
	self.graduation = nbd.StringProperty()
	self.curr_college = nbd.StringProperty()
	self.past_colleges = nbd.StringProperty() #list
	self.highschool = nbd.StringProperty()
	self.profile_picture = nbd.BlobProperty() #default not indexed
	self.curr_job = nbd.StringProperty()
	self.past_job = nbd.StringProperty()
	self.about = nbd.TextProperty() #default not indexed
	self.approach_status = nbd.StringProperty()

	def __init__(self, profile_dict):
		self.key = nbd.Key(profile_dict['profile_type'], profile_dict['email'])
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