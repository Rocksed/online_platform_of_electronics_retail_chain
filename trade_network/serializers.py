from rest_framework import serializers

from trade_network.models import FactoryElements, ElementsRetail, ElementsIE


class FactorySerializers(serializers.ModelSerializer):
    class Meta:
        model = FactoryElements
        fields = '__all__'
