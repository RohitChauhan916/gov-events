from rest_framework import serializers
from country.models import country

class ItemSerialzer(serializers.ModelSerializer):
    class Meta:
        model = country
        fields = '__all__'