from django.contrib.auth.models import User, Group
from rest_framework import serializers

from api.models import Case


class CaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Case
        fields = ['city_name', 'confirmed', 'dead', 'recovered', 'lat', 'lon']
