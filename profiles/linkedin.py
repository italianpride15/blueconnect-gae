class LinkedinProfile(BaseProfile, BaseDatastore):
	
	def __init__(self, object):
		self.id = object.profile_type
		self.email = object.email
		self.full_name = object.full_name
		self.qualities = object.qualities #list
		self.connections = object.connections #list
		self.address = object.address
		self.curr_classes = object.curr_classes #list, edu only
		self.past_classes = object.past_classes #list, linkedin/old edu
		self.major = object.major
		self.minor = object.minor
		self.graduation = object.graduation
		self.curr_college = object.curr_college
		self.past_colleges = object.past_colleges #list
		self.highschool = object.highschool
		self.profile_picture = object.profile_picture
		self.curr_job = object.curr_job
		self.past_job = object.past_job
		self.about = object.about
		self.approach_status = object.approach_status

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