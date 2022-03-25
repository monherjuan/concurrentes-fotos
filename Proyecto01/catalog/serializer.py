from rest_framework import serializers
from catalog.models import modelUsuario


class userSerializer (serializers.ModelSerializer) :

    class meta:
        model = modelUsuario
        fields = ("id","name","email","password")
        