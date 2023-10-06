from rest_framework import viewsets

from trade_network.models import FactoryElements
from trade_network.serializers import FactorySerializers


class FactoryViewSet(viewsets.ModelViewSet):
    queryset = FactoryElements.objects.all()
    serializer_class = FactorySerializers


