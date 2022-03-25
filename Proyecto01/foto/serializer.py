from rest_framework import serializers
from foto.models import fotoModel



class fotoUser (serializers.ModelSerializer):

    class meta:
        model = fotoModel
        field = ('url')