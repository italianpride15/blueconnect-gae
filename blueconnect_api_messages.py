"""ProtoRPC message class definitions for BlueConnect API."""
import endpoints
from protorpc import messages


class ProfileMessage(messages.Message):
    """ProtoRPC message definition to represent a BlueConnect profile"""
    profile_type = messages.StringField(1)
    username = messages.StringField(2)
    email = messages.StringField(3)
    full_name = messages.StringField(4)
    qualities = messages.StringField(5)
    connections = messages.StringField(6)
    address = messages.StringField(7)
    curr_classes = messages.StringField(8)
    past_classes = messages.StringField(9)
    major = messages.StringField(10)
    minor = messages.StringField(11)
    graduation = messages.StringField(12)
    curr_college = messages.StringField(13)
    past_colleges = messages.StringField(14)
    highschool = messages.StringField(15)
    profile_picture = messages.StringField(16)
    curr_job = messages.StringField(17)
    past_job = messages.StringField(18)
    about = messages.StringField(19)
    approach_status = messages.StringField(20)

class GeneralResponse(messages.Message):
    """Response that stores a message."""
    message = messages.StringField(1)