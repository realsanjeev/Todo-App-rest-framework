from rest_framework.authentication import TokenAuthentication as BaseAuth

class TokenAutentication(BaseAuth):
    keyword = "Bearer"
