from rest_framework.authentication import TokenAuthentication as BaseAuth


class TokenAutentication(BaseAuth):
    """Default is Token"""

    keyword = "Bearer"
