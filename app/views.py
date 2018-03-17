from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSerializer


class UserListView(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class LoggedInUserView(APIView):

    def get(self, request, format=None):
        if isinstance(request.user, get_user_model()):
            serializer = UserSerializer(request.user)
            return Response(serializer.data)
        else:
            return Response({"error": "no user is logged in."})
