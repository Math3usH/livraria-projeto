
from rest_framework.viewsets import ModelViewSet

from core.serializers import CategoriaSerialaizer

from core.serializers import categoria

class categoriaViewSet(ModelViewSet):
    query = categoria.objects.all()
    serializer_class = CategoriaSerialaizer