from rest_framework import serializers
from .models import Programmer

class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        # fields = ("fullname", "nickname",) # Pueden colorcarse los que se requieren
        fields = "__all__"
