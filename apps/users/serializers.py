from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    """User registration serializer"""

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "email",
            "phone",
            "user_type",
            "specialization",
            "description",
            "contact",
        ]
        read_only_fields = ['is_active']
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()

        return user


class LoginUserSerializer(serializers.ModelSerializer):
    """Login user serializer"""

    class Meta:
        model = User
        fields = [
            "email",
            "password"
        ]

