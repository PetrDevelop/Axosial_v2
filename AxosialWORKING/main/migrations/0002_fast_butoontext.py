# Generated by Django 5.0.2 on 2024-03-01 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fast',
            name='butoonText',
            field=models.CharField(default='Читать', max_length=25, verbose_name='Текст кнопки читать'),
        ),
    ]
