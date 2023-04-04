from rest_framework import serializers

from .models import PDF



class PDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDF
        fields = '__all__'
        read_only_fields = ('id', 'size', 'number_of_pages', 'parsing_status', 'time_of_upload')


class NewPDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDF
        exclude = ['number_of_pages']


class UploadPDFSerializer(serializers.Serializer):
    file = serializers.ListField(child=serializers.FileField(), allow_empty=False)

    def create(self, validated_data):
        files = validated_data.pop('file')
        for f in files:
           pdf = PDF.objects.create(pdf_file=f, size=f.size)
        return pdf