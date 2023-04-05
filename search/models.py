from django.db import models


class PDFSearch(models.Model):
    pdf = models.ForeignKey('pdf.PDF', on_delete=models.CASCADE)
    sentence = models.TextField()
    
    @property
    def length(self):
        return len(self.sentence)
    
    def __str__(self) -> str:
        return f'{self.pdf_id}'
