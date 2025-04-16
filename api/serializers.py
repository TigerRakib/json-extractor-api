from rest_framework import serializers

class ImageSerializer(serializers.Serializer):
    imageBase64 = serializers.CharField()
