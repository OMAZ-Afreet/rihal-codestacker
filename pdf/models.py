from django.db import models


class PDF(models.Model):
    pdf_file = models.FileField()
    time_of_upload = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.pdf_file.name
    