from rest_framework import viewsets
from foto.models import fotoModel
from foto.serializer import fotoUser


class fotoView (viewsets.ModelViewSet):

    queryset = fotoModel.objects.all()
    serializer_class = fotoUser

    