from rest_framework import viewsets
from catalog.models import modelUsuario
from catalog.serializer import userSerializer


class viewUser (viewsets.ModelViewSet):

    queryset = modelUsuario.objects.all()
    serializer_class = userSerializer
