from rest_framework import serializers
from jokes.models import Joke

class JokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joke
        fields=('id','content','author')