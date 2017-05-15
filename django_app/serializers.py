from rest_framework_mongoengine import serializers
from .models import ScrapyItems

class ScrapyItemsSerializer(serializers.DocumentSerializer):
    class Meta:
        model = ScrapyItems
        fields = ['article_title', 'article_tag', 'article_heading', 'article_text', 'article_url']



