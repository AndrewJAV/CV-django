# Generated by Django 5.0.7 on 2024-08-12 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='end_date',
            field=models.CharField(default='Presente', max_length=10),
        ),
    ]
