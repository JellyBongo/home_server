from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions


class TokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = request.user
        if not username:
            return None

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)
