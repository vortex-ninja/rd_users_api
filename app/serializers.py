from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {
            'password': {
                            'write_only': True,
                            'style': {'input_type': 'password'},
                    },
        }

    def create(self, validated_data):
        model = get_user_model()
        print(model.te)
        print(model.objects.create_user)
        user = model.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
