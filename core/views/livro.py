from rest_framework.viewsets import ModelViewSet

from core.serializers import LivroSerializer

from core.models import LivroSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializers

