from .models import Perro
from rest_framework import serializers

class PerroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perro
        fields = ('nombre','raza','descripcion','estado')