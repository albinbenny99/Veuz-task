from rest_framework import serializers
from .models import CustomUser, Employee

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class EmployeeSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create(**user_data)
        employee = Employee.objects.create(user=user, **validated_data)
        return employee
