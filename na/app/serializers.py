from rest_framework import serializers
from app.models import Feed

class postSerializer(serializers.ModelSerializer):
	class Meta:
		model = Feed
		fields = "__all__"