from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets

# Create your views here.
from api.models import Case
from api.serializers import CaseSerializer


class CaseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    http_method_names = ['get']
