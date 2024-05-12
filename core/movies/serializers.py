from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movie
		fields = ['id', 'title', 'description', 'release_date', 'genres', 'avg_rating', 'poster']