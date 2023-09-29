from rest_framework import serializers
from .models import *

class TovarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tovar
        fields = ('title', 'text', 'made', 'date', 'img', 'cat', 'id')