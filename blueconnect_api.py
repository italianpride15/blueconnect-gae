import endpoints
import webapp2
from protorpc import remote
from protorpc import messages
from protorpc import message_types

from blueconnect_api_messages import ProfileMessage
from blueconnect_api_messages import GeneralResponse

from helpers.endpointsinterfacetodatastore import EndpointsInterfaceToDatastore


#webapp2 for handling Admin Console
#class Admin(webapp2.RequestHandler):
#  pass
#app = webapp2.WSGIApplication('/admin', Admin, debug=True)


@endpoints.api(name='blueconnect', version='v1', description='Blue-Connect API') #allowed_client_ids=[...,...]
class BlueConnect(remote.Service):
    """Class that defines Blue-Connect API"""


    USERNAME_RESOURCE = endpoints.ResourceContainer(
            message_types.VoidMessage,
            profile_type = messages.StringField(1, required=True),
            username = messages.StringField(2, required=True))

    @endpoints.method(USERNAME_RESOURCE, ProfileMessage,
                      path='profile/{profile_type}/{username}', http_method='GET',
                      name='profile.get')
    def profile_get(self, request):
        profile_type = request.profile_type
        username = request.username
        user = EndpointsInterfaceToDatastore.get_profile(profile_type, username)
        return ProfileMessage(profile_type=profile_type, user=user)
    
    @endpoints.method(USERNAME_RESOURCE, GeneralResponse,
                      path='profile/{profile_type}/{username}', http_method='DELETE',
                      name='profile.delete')
    def profile_delete(self, request):
        profile_type = request.profile_type
        username = request.username
        response = EndpointsInterfaceToDatastore.delete_profile(profile_type, username)
        return GeneralResponse(message=response)


    PROFILE_RESOURCE = endpoints.ResourceContainer(
            ProfileMessage,
            profile_type = messages.StringField(1))

    @endpoints.method(PROFILE_RESOURCE, GeneralResponse,
                      path ='profile/{profile_type}', http_method='POST',
                      name='profile.post')
    def profile_post(self, request):
        profile_type = request.profile_type
        profile_dict = request.profile_dict
        response = EndpointsInterfaceToDatastore.post_profile(profile_type, profile_dict)
        return GeneralResponse(message=response)

    @endpoints.method(PROFILE_RESOURCE, GeneralResponse,
                      path='profile/{profile_type}', http_method='PUT',
                      name='profile.put')
    def profile_put(self, request):
        profile_type = request.profile_type
        profile_dict = request.profile_dict
        response = EndpointsInterfaceToDatastore.put_profile(profile_type, profile_dict)
        return GeneralResponse(message=response)


app = endpoints.api_server([BlueConnect])