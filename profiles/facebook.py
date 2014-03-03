from baseclasses import BaseProfile
from baseclasses import BaseDatastore

class FacebookProfile(BaseProfile, BaseDatastore):

	#might want to include @properties for getters/setters
	def __init__(self, profile_dict):
		self.id = profile_dict['profile_type']
		self.email = profile_dict['email']
		self.full_name = profile_dict['full_name']
		self.qualities = profile_dict['qualities'] #list
		self.connections = profile_dict['connections'] #list
		self.address = profile_dict['address']
		self.curr_classes = profile_dict['curr_classes'] #list, edu only
		self.past_classes = profile_dict['past_classes'] #list, linkedin/old edu
		self.major = profile_dict['major']
		self.minor = profile_dict['minor']
		self.graduation = profile_dict['graduation']
		self.curr_college = profile_dict['curr_college']
		self.past_colleges = profile_dict['past_colleges'] #list
		self.highschool = profile_dict['highschool']
		self.profile_picture = profile_dict['profile_picture']
		self.curr_job = profile_dict['curr_job']
		self.past_job = profile_dict['past_job']
		self.about = profile_dict['about']
		self.approach_status = profile_dict['approach_status']

	@classmethod
	def post_profile(self):
		"""Profile creates a new instance of itself."""
	
	@classmethod
	def get_profile(self):
		"""Profile returns itself."""

	@classmethod
	def put_profile(self):
		"""Profile updates itself."""

	@classmethod
	def delete_profile(self):
		"""Profile deletes itself."""
		#super(FacebookProfile, self).delete_profile()