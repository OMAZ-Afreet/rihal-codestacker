# Generated by Django 4.2 on 2023-04-04 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pdf", "0004_pdf_number_of_pages_pdf_parsing_status_pdf_size"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pdf",
            name="number_of_pages",
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
