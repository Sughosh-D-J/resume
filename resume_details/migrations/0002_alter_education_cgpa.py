# Generated by Django 4.1.7 on 2023-04-22 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_details', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='cgpa',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True),
        ),
    ]
