from django.core.urlresolvers import reverse
from django.shortcuts import render

#from allaccess.views import OAuthRedirect
#from allaccess.views import OAuthCallback

def home(request):
    "Simple homepage view"
    context = {}
    if request.user.is_authenticated():
        try:
            access = request.user.accountaccess_set.all()[0]
        except IndexError:
            access = None
        else:
            client = access.api_client
            context['info'] = client.get_profile_info(raw_token=access.access_token)
    return render(request, 'home.html', context)
        

#class AdditionalPermissionsRedirect(OAuthRedirect):

#    def get_callback_url(self, provider):
#        return reverse('fflogin', kwargs={'provider': provider.name})

#    def get_additional_parameters(self, provider):
#        if provider.name == 'facebook':
#            # Request permission to see user's email
#            return {
#                    'scope': 'email',
#                    }
#        return super(AdditionalPermissionsRedirect, self).get_additional_parameters(provider)

#class FloginCallback(OAuthCallback):
    
#    def get_or_create_user(self, provider, access, info):
#        return self.request.user

#    def handle_existing_user(self, provider, user, access, info):
#        if user != self.request.user:
#            return self.handle_login_failure(provider, "Nada")
#        return super(FloginCallback, self).handle_existing_user(provider, user, access, info)
#
#    def get_user_id(self, provider, info):
#        return info

#class AssociateCallback(OAuthCallback):
#
#    def get_or_create_user(self, provider, access, info):
#        return self.request.user
#
#    def handle_existing_user(self, provider, user, access, info):
#        if user != self.request.user:
#            return self.handle_login_failure(provider, "Hay otro usuario asociado con esta cuenta")
#        # User was already associated with this account
#        return super(AssociateCallback, self).handle_existing_user(provider, user, access, info)
#
#class AssociateRedirect(OAuthRedirect):
#
#    def get_callback_url(self, provider):
#        return reverse('associate-callback', kwargs={'provider': provider.name})
