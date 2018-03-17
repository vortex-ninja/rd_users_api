from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer
from .tokens import jwt_payload_handler, jwt_encode_handler


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


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    # I add the token when user creation was succesful and response is ready

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        # Get the created user instance

        created_user = get_user_model().objects.get(pk=serializer.data['id'])

        # Create token for newly created user

        payload = jwt_payload_handler(created_user)
        token = jwt_encode_handler(payload)

        # Include token in the response

        response = {"created_user": serializer.data, "token" : token}

        return Response(response, status=status.HTTP_201_CREATED, headers=headers)
