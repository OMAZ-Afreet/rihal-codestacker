from django.db import models


class PDF(models.Model):
    pdf_file = models.FileField(unique=True)
    size = models.PositiveBigIntegerField()
    number_of_pages = models.PositiveSmallIntegerField(default=0)
    
    PS = (
        ('IN PROCESS', 'IN PROCESS'),
        ('DONE', 'DONE'),
        ('FAILED', 'FAILED'),
    )
    parsing_status = models.CharField(max_length=10, choices=PS, default='IN PROCESS')
    time_of_upload = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.pdf_file.name
