from rest_framework import serializers
from rest_framework.fields import CharField
from phonenumber_field.serializerfields import PhoneNumberField

class UserRegisterSerializer(serializers.Serializer):
    name = serializers.CharField()
    phoneNumber = PhoneNumberField()
    pinCode = serializers.IntegerField()


class UserAssessmentSerializer(serializers.Serializer):
    userId = serializers.CharField()
    symptoms = serializers.ListField()
    travelHistory = serializers.BooleanField()
    contactWithCovidPatient = serializers.BooleanField()


class UserCovidResultSerializer(serializers.Serializer):
    userId = serializers.CharField()
    adminId = serializers.CharField()
    result = serializers.CharField()

