# Generated by Django 4.1.7 on 2023-04-24 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_details', '0008_certification_certificate_id_certification_duration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='name',
            field=models.CharField(max_length=500),
        ),
    ]
