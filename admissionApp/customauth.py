from typing_extensions import Required
from rest_framework.autentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AutenticationFailed

class authentication(BaseAuthentication):
    def authentication(self,request):
        username=request.GET.get('username')
        if username is None:
            return none
        try:
            User=User.objects.get(username=username)
        except User.DoesNotExist:
                raise authenticationFailed('No Such User')
                return(user,None)
                
