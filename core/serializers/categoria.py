
from rest_framework.serializers import ModelSerializer

from core.models import categoria

class CategoriaSerialaizer(ModelSerializer):
    class Meta:
        model = categoria 
        fields = "__all__"