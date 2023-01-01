from rest_framework import serializers
from .models import CrudAPI

class CrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrudAPI
        fields = ['id', 'title', 'sub_title', 'description']