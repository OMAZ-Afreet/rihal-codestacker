from rest_framework import serializers

from .models import PDF


class PDFSerializer(serializers.ModelSerializer):
    file_name = serializers.FileField(source='pdf_file')
    class Meta:
        model = PDF
        exclude = ['parsing_status', 'pdf_file']
        read_only_fields = ('id', 'size', 'number_of_pages', 'time_of_upload')


class NewPDFSerializer(serializers.ModelSerializer):
    file_name = serializers.FileField(source='pdf_file')
    class Meta:
        model = PDF
        exclude = ['number_of_pages', 'pdf_file']


class UploadPDFSerializer(serializers.Serializer):
    file = serializers.ListField(child=serializers.FileField(), allow_empty=False)

    def create(self, validated_data):
        files = validated_data.pop('file')
        for f in files:
           pdf = PDF.objects.create(pdf_file=f, size=f.size)
        return pdf