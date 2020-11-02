from rest_framework import serializers
from .models import Ashish

class AshishSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ashish
        fields='__all__'