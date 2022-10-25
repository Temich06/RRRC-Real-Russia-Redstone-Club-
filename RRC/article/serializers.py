from rest_framework import serializers
from article.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id',
                  'title',
                  'description',
                  'date',
                  'author',
                  'mcversion',
                  'download_link',
                  'clock_time',
                  'img',]