# Generated by Django 4.2 on 2023-04-03 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pdf", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="pdf",
            old_name="file",
            new_name="pdf_file",
        ),
    ]
