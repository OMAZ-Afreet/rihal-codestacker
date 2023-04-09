from rest_framework import serializers

from .models import PDFSearch

class PDFSearchSerializer(serializers.ModelSerializer):
    pdf_ID = serializers.PrimaryKeyRelatedField(source='pdf', read_only=True)
    class Meta:
        model = PDFSearch
        fields = ['pdf_ID', 'sentence']


class SearchSerializer(serializers.Serializer):
    search = serializers.CharField(allow_blank=False)
    


class AdvancedSearchSerializer(serializers.Serializer):
    mode = serializers.CharField()
    count = serializers.IntegerField()
    results = PDFSearchSerializer(many=True)