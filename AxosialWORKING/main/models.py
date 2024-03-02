from django.db import models
import datetime
# Create your models here.
class Fast(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)

    text = models.TextField('Текст блога')

    buttonText = models.CharField('Текст кнопки читать', default='Читать', max_length=25)
    date = models.DateField("Date", default=datetime.date.today)


    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = "публикации"


    def __str__(self):
        return self.title



