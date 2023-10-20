from django.db import models

class Weather(models.Model):
	city_name = models.CharField(u'Город', max_length=255)
	temperature = models.FloatField(u'Температура', blank=True, null=True, help_text="градусов Цельсия")
	pressure = models.FloatField(u'Давление', blank=True, null=True, help_text="мм.рт.ст")
	wind = models.FloatField(u'Скорость ветра', blank=True, null=True, help_text="м/с")
	date_created = models.DateTimeField(u'Дата создания', auto_now_add=True)

	def __str__(self):
	    return self.city_name

	class Meta:
		verbose_name = u"Прогноз Погоды"
		verbose_name_plural  = u"Прогнозы Погоды"