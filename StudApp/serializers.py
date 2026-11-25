from rest_framework import serializers
from django.contrib.auth.models import User
from StudApp.models import StudentDb

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=["id","username","email","password"]

    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        return user

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentDb
        fields="__all__"
