from rest_framework import serializers
from .models import Company,Job,Application,Userprofile

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields='__all__'
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job
        fields='__all__'
class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Application
        fields='__all__'
class UserprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Userprofile
        fields='__all__'