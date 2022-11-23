from rest_framework import viewsets


from.models import *
from.serializers import *

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
